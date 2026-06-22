#include <parallel/algorithm>
#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <mutex>
#include <stdexcept>
#include <unordered_map>
#include <vector>
#include <omp.h>
#include "logsM.hpp"
static constexpr uint64_t KAP=15337197211725320908ULL,S0=7668598605862660454ULL,S1=15778797251807138534ULL,HALF=MOD/2;
static inline uint64_t addm(uint64_t a,uint64_t b){__uint128_t z=(__uint128_t)a+b;if(z>=MOD)z-=MOD;return(uint64_t)z;}
static inline uint64_t subm(uint64_t a,uint64_t b){return a>=b?a-b:(uint64_t)((__uint128_t)a+MOD-b);}
static inline uint64_t mix(uint64_t x){x+=0x9e3779b97f4a7c15ULL;x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL;x=(x^(x>>27))*0x94d049bb133111ebULL;return x^(x>>31);}
static int tauk(int k){int i=k/16+1,a=k%16;if(i==1)return 16+(a+6)%16;if(i==2)return(a+10)%16;return 32+(a+8)%16;}
struct Tr{uint64_t d;uint8_t c,k6,k7;};struct Dup{uint64_t key;uint16_t count;int shard;};
template<class F>static void circular_slice(const std::vector<uint64_t>&v,uint64_t start,uint64_t L,uint64_t U,F&&fn){
 if(L>=U)return;__uint128_t aa=(__uint128_t)start+L,bb=(__uint128_t)start+U;uint64_t a=(uint64_t)(aa%MOD),b=(uint64_t)(bb%MOD);
 if(aa/MOD==((bb-1)/MOD)){auto i=std::lower_bound(v.begin(),v.end(),a),j=(b==0?v.end():std::lower_bound(v.begin(),v.end(),b));for(auto p=i;p!=j;++p)fn(*p);}
 else{auto i=std::lower_bound(v.begin(),v.end(),a);for(auto p=i;p!=v.end();++p)fn(*p);auto j=std::lower_bound(v.begin(),v.end(),b);for(auto p=v.begin();p!=j;++p)fn(*p);}
}
int main(int argc,char**argv){
 const int SH=argc>1?std::atoi(argv[1]):16384,THREADS=argc>2?std::atoi(argv[2]):16;const size_t CAP=1ULL<<22,MASK=CAP-1;if(SH!=16384)throw std::runtime_error("optimized checker expects 16384 shards");
 auto w0=std::chrono::steady_clock::now();uint64_t kap=0;for(int t=0;t<7;t++){uint64_t kt=addm(LOGS[t][0],LOGS[t][tauk(0)]);for(int k=0;k<48;k++){if(tauk(tauk(k))!=k||tauk(k)==k)throw std::runtime_error("tau involution");if(addm(LOGS[t][k],LOGS[t][tauk(k)])!=kt)throw std::runtime_error("tau log");if(((COLORS[t][k]+COLORS[t][tauk(k)])&15)!=8)throw std::runtime_error("tau color");}kap=addm(kap,kt);}if(kap!=KAP||addm(S0,S0)!=KAP||addm(S1,S1)!=KAP)throw std::runtime_error("tau constants");
 std::vector<int> H;for(int k=0;k<48;k++)if(k<tauk(k))H.push_back(k);if(H.size()!=24)throw std::runtime_error("orientation");
 std::array<std::vector<uint64_t>,16>base;std::array<size_t,16>cnt{};for(int a:H)for(int b=0;b<48;b++)for(int c=0;c<48;c++)for(int d=0;d<48;d++)for(int e=0;e<48;e++)cnt[(COLORS[0][a]+COLORS[1][b]+COLORS[2][c]+COLORS[3][d]+COLORS[4][e])&15]++;for(int c=0;c<16;c++)base[c].reserve(cnt[c]);
 for(int a:H)for(int b=0;b<48;b++)for(int c=0;c<48;c++){uint64_t s3=addm(addm(LOGS[0][a],LOGS[1][b]),LOGS[2][c]);int c3=(COLORS[0][a]+COLORS[1][b]+COLORS[2][c])&15;for(int d=0;d<48;d++){uint64_t s4=addm(s3,LOGS[3][d]);int c4=(c3+COLORS[3][d])&15;for(int e=0;e<48;e++)base[(c4+COLORS[4][e])&15].push_back(addm(s4,LOGS[4][e]));}}
 auto w1=std::chrono::steady_clock::now();for(int c=0;c<16;c++){__gnu_parallel::sort(base[c].begin(),base[c].end());for(size_t i=1;i<base[c].size();i++)if(base[c][i]==base[c][i-1])throw std::runtime_error("five-slot same-color collision");}auto w2=std::chrono::steady_clock::now();
 std::vector<Tr>tr;for(int f=0;f<48;f++)for(int g=0;g<48;g++)tr.push_back({addm(LOGS[5][f],LOGS[6][g]),(uint8_t)((COLORS[5][f]+COLORS[6][g])&15),(uint8_t)f,(uint8_t)g});uint64_t expected=0;for(auto&q:tr)expected+=base[(4-q.c)&15].size();if(expected!=26373783552ULL)throw std::runtime_error("domain count");
 uint64_t fixed0=0,fixed1=0;for(auto&q:tr){auto&v=base[(4-q.c)&15];fixed0+=std::binary_search(v.begin(),v.end(),subm(S0,q.d));fixed1+=std::binary_search(v.begin(),v.end(),subm(S1,q.d));}
 std::atomic<int>done{0};std::atomic<uint64_t>entries{0},energy{0};std::atomic<uint16_t>gmax{0};std::mutex mu;std::vector<Dup>dups;
 auto w3=std::chrono::steady_clock::now();
 #pragma omp parallel num_threads(THREADS)
 {
  std::vector<uint64_t>tab(CAP,std::numeric_limits<uint64_t>::max());std::vector<uint32_t>used;used.reserve(1800000);std::unordered_map<uint64_t,uint16_t>dc;dc.reserve(32);
  #pragma omp for schedule(dynamic,1)
  for(int shard=0;shard<SH;shard++){
   uint64_t lo=(uint64_t)((__uint128_t)HALF*shard/SH),hi=(uint64_t)((__uint128_t)HALF*(shard+1)/SH);uint64_t L2=MOD-hi+1;__uint128_t uu=(__uint128_t)MOD-lo+1;uint64_t U2=uu>MOD?MOD:(uint64_t)uu;uint64_t acc=0,en=0;uint16_t mx=1;dc.clear();used.clear();
   auto ins=[&](uint64_t b,uint64_t d){uint64_t x=addm(b,d),z=subm(x,S0),r=std::min(z,MOD-z);if(!(lo<=r&&r<hi))throw std::runtime_error("range");acc++;size_t p=mix(r)&MASK;for(;;){uint64_t q=tab[p];if(q==std::numeric_limits<uint64_t>::max()){tab[p]=r;used.push_back((uint32_t)p);return;}if(q==r){auto[it,isnew]=dc.emplace(r,1);uint16_t old=it->second;en+=2ULL*old;it->second=old+1;mx=std::max(mx,it->second);return;}p=(p+1)&MASK;}};
   for(auto&q:tr){auto&v=base[(4-q.c)&15];uint64_t st=subm(S0,q.d);circular_slice(v,st,lo,hi,[&](uint64_t b){ins(b,q.d);});if(L2<MOD&&L2<U2)circular_slice(v,st,L2,U2,[&](uint64_t b){ins(b,q.d);});}
   if(used.size()>CAP*3/5)throw std::runtime_error("hash load too high");for(uint32_t p:used)tab[p]=std::numeric_limits<uint64_t>::max();entries.fetch_add(acc,std::memory_order_relaxed);energy.fetch_add(en,std::memory_order_relaxed);uint16_t old=gmax.load();while(mx>old&&!gmax.compare_exchange_weak(old,mx));
   if(!dc.empty()){std::lock_guard<std::mutex>lk(mu);for(auto&kv:dc)dups.push_back({kv.first,kv.second,shard});}
   int z=done.fetch_add(1)+1;if((z&1023)==0||z==SH){std::lock_guard<std::mutex>lk(mu);std::cerr<<"progress "<<z<<"/"<<SH<<" entries="<<entries.load()<<" energy="<<energy.load()<<" max="<<gmax.load()<<"\n";}
  }
 }
 auto w4=std::chrono::steady_clock::now();std::sort(dups.begin(),dups.end(),[](auto&a,auto&b){return a.key<b.key;});uint64_t checkE=0;uint16_t checkM=1;for(auto&d:dups){checkE+=(uint64_t)d.count*(d.count-1);checkM=std::max(checkM,d.count);}if(checkE!=energy.load()||checkM!=gmax.load())throw std::runtime_error("duplicate summary mismatch");uint64_t projectedMax=std::max<uint64_t>(gmax.load(),2*std::max(fixed0,fixed1));bool pass=entries.load()==expected&&fixed0==0&&fixed1==0&&projectedMax<=12&&energy.load()<=154;
 auto sec=[](auto a,auto b){return std::chrono::duration<double>(b-a).count();};std::cout<<"{\n  \"decision\": \""<<(pass?"TAU_FOLDED_PROJECTED_MMAX_LE_12":"FAIL")<<"\",\n  \"projection_modulus\": "<<MOD<<",\n  \"kernel_order\": 3,\n  \"kappa\": "<<KAP<<",\n  \"fixed_roots\": ["<<S0<<", "<<S1<<"],\n  \"fixed_selected_counts\": ["<<fixed0<<", "<<fixed1<<"],\n  \"tau_half_domain_expected\": "<<expected<<",\n  \"tau_half_domain_counted\": "<<entries.load()<<",\n  \"canonical_shards\": "<<SH<<",\n  \"threads\": "<<THREADS<<",\n  \"folded_ordered_energy\": "<<energy.load()<<",\n  \"projected_ordered_energy\": "<<2*energy.load()<<",\n  \"max_canonical_projected_multiplicity\": "<<gmax.load()<<",\n  \"full_projected_max_including_fixed\": "<<projectedMax<<",\n  \"duplicate_canonical_bins\": [\n";for(size_t i=0;i<dups.size();i++){auto&d=dups[i];std::cout<<"    {\"key\": "<<d.key<<", \"count\": "<<d.count<<", \"shard\": "<<d.shard<<"}"<<(i+1==dups.size()?"":",")<<"\n";}std::cout<<"  ],\n  \"seconds\": {\"generate_base\": "<<sec(w0,w1)<<", \"sort_base\": "<<sec(w1,w2)<<", \"setup\": "<<sec(w2,w3)<<", \"scan\": "<<sec(w3,w4)<<", \"total\": "<<sec(w0,w4)<<"}\n}\n";return pass?0:1;
}
