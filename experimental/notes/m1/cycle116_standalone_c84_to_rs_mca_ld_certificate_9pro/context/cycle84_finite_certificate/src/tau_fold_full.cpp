#include <parallel/algorithm>
#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <limits>
#include <mutex>
#include <stdexcept>
#include <unordered_map>
#include <vector>
#include <omp.h>
#include "logsM.hpp"

static constexpr uint64_t KAP=15337197211725320908ULL;
static constexpr uint64_t S0=7668598605862660454ULL;
static constexpr uint64_t S1=15778797251807138534ULL;
static constexpr uint64_t HALF=MOD/2;
static inline uint64_t addm(uint64_t a,uint64_t b){__uint128_t z=(__uint128_t)a+b;if(z>=MOD)z-=MOD;return(uint64_t)z;}
static inline uint64_t subm(uint64_t a,uint64_t b){return a>=b?a-b:(uint64_t)((__uint128_t)a+MOD-b);}
static inline uint64_t mix(uint64_t x){x+=0x9e3779b97f4a7c15ULL;x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL;x=(x^(x>>27))*0x94d049bb133111ebULL;return x^(x>>31);}
static int tauk(int k){int i=k/16+1,a=k%16;if(i==1)return 16+(a+6)%16;if(i==2)return(a+10)%16;return 32+(a+8)%16;}
struct Tr{uint64_t d;uint8_t c;uint8_t k6,k7;};

template<class F> static size_t circular_slice(const std::vector<uint64_t>&v,uint64_t start,uint64_t L,uint64_t U,F&&fn){
 if(L>=U)return 0;__uint128_t aa=(__uint128_t)start+L,bb=(__uint128_t)start+U;uint64_t a=(uint64_t)(aa%MOD),b=(uint64_t)(bb%MOD);size_t n=0;
 if(aa/MOD==((bb-1)/MOD)){
  auto i=std::lower_bound(v.begin(),v.end(),a),j=(b==0?v.end():std::lower_bound(v.begin(),v.end(),b));
  for(auto p=i;p!=j;++p){fn(*p);++n;}
 }else{
  auto i=std::lower_bound(v.begin(),v.end(),a);for(auto p=i;p!=v.end();++p){fn(*p);++n;}
  auto j=std::lower_bound(v.begin(),v.end(),b);for(auto p=v.begin();p!=j;++p){fn(*p);++n;}
 }
 return n;
}
static size_t count_slice(const std::vector<uint64_t>&v,uint64_t start,uint64_t L,uint64_t U){
 if(L>=U)return 0;__uint128_t aa=(__uint128_t)start+L,bb=(__uint128_t)start+U;uint64_t a=(uint64_t)(aa%MOD),b=(uint64_t)(bb%MOD);
 if(aa/MOD==((bb-1)/MOD)){auto i=std::lower_bound(v.begin(),v.end(),a),j=(b==0?v.end():std::lower_bound(v.begin(),v.end(),b));return(size_t)(j-i);}
 auto i=std::lower_bound(v.begin(),v.end(),a),j=std::lower_bound(v.begin(),v.end(),b);return(size_t)((v.end()-i)+(j-v.begin()));
}
static uint64_t interval_lo2(uint64_t hi){return MOD-hi+1;}
static uint64_t interval_hi2(uint64_t lo){__uint128_t u=(__uint128_t)MOD-lo+1;return u>MOD?MOD:(uint64_t)u;}

int main(int argc,char**argv){
 const int SH=argc>1?std::atoi(argv[1]):4096;const int THREADS=argc>2?std::atoi(argv[2]):8;if(SH<=0||THREADS<=0)return 2;
 auto wall0=std::chrono::steady_clock::now();
 // Validate the tau constants directly from the table.
 uint64_t kap=0;for(int t=0;t<7;t++){uint64_t kt=addm(LOGS[t][0],LOGS[t][tauk(0)]);for(int k=1;k<48;k++)if(addm(LOGS[t][k],LOGS[t][tauk(k)])!=kt)throw std::runtime_error("tau slot constant failure");kap=addm(kap,kt);}if(kap!=KAP||addm(S0,S0)!=KAP||addm(S1,S1)!=KAP)throw std::runtime_error("kappa/root failure");
 std::vector<int> H;for(int k=0;k<48;k++)if(k<tauk(k))H.push_back(k);if(H.size()!=24)throw std::runtime_error("orientation failure");
 std::array<std::vector<uint64_t>,16> base;std::array<size_t,16> cnt{};
 // Exact color counts, then fill the oriented five-slot lists.
 for(int a:H)for(int b=0;b<48;b++)for(int c=0;c<48;c++)for(int d=0;d<48;d++)for(int e=0;e<48;e++)cnt[(COLORS[0][a]+COLORS[1][b]+COLORS[2][c]+COLORS[3][d]+COLORS[4][e])&15]++;
 for(int c=0;c<16;c++)base[c].reserve(cnt[c]);
 for(int a:H)for(int b=0;b<48;b++)for(int c=0;c<48;c++){
  uint64_t s3=addm(addm(LOGS[0][a],LOGS[1][b]),LOGS[2][c]);int c3=(COLORS[0][a]+COLORS[1][b]+COLORS[2][c])&15;
  for(int d=0;d<48;d++){uint64_t s4=addm(s3,LOGS[3][d]);int c4=(c3+COLORS[3][d])&15;for(int e=0;e<48;e++)base[(c4+COLORS[4][e])&15].push_back(addm(s4,LOGS[4][e]));}
 }
 auto wall1=std::chrono::steady_clock::now();
 for(int c=0;c<16;c++){__gnu_parallel::sort(base[c].begin(),base[c].end());if(base[c].size()!=cnt[c])throw std::runtime_error("base size failure");for(size_t i=1;i<base[c].size();i++)if(base[c][i]==base[c][i-1])throw std::runtime_error("oriented five-slot projection collision");}
 auto wall2=std::chrono::steady_clock::now();
 std::vector<Tr> tr;tr.reserve(2304);for(int f=0;f<48;f++)for(int g=0;g<48;g++)tr.push_back({addm(LOGS[5][f],LOGS[6][g]),(uint8_t)((COLORS[5][f]+COLORS[6][g])&15),(uint8_t)f,(uint8_t)g});
 uint64_t expected=0;for(auto&q:tr)expected+=(uint64_t)base[(4-q.c)&15].size();if(expected!=26373783552ULL)throw std::runtime_error("half-domain count failure");
 // Fixed projected bins: selected-half counts; full counts would be twice these.
 uint64_t fixed0=0,fixed1=0;for(auto&q:tr){auto&v=base[(4-q.c)&15];fixed0+=std::binary_search(v.begin(),v.end(),subm(S0,q.d));fixed1+=std::binary_search(v.begin(),v.end(),subm(S1,q.d));}
 std::atomic<int> done{0};std::atomic<uint64_t> entries{0};std::atomic<uint64_t> energy{0};std::atomic<uint16_t> global_max{0};std::atomic<uint64_t> global_key{0};std::atomic<int> global_shard{-1};std::mutex outmu;
 auto process_shard=[&](int shard){
  uint64_t lo=(uint64_t)((__uint128_t)HALF*shard/SH),hi=(uint64_t)((__uint128_t)HALF*(shard+1)/SH),L2=interval_lo2(hi),U2=interval_hi2(lo);
  size_t total=0;for(auto&q:tr){auto&v=base[(4-q.c)&15];uint64_t st=subm(S0,q.d);total+=count_slice(v,st,lo,hi);if(L2<MOD&&L2<U2)total+=count_slice(v,st,L2,U2);}
  size_t cap=1;while(cap<(size_t)(total*1.35)+16)cap<<=1;std::vector<uint64_t> tab(cap,std::numeric_limits<uint64_t>::max());std::unordered_map<uint64_t,uint16_t> dup;dup.reserve(32);uint64_t en=0,acc=0;uint16_t mx=1;uint64_t mxkey=0;
  auto ins=[&](uint64_t b,uint64_t d){uint64_t x=addm(b,d),z=subm(x,S0),r=std::min(z,MOD-z);if(!(lo<=r&&r<hi))throw std::runtime_error("canonical range failure");acc++;size_t p=mix(r)&(cap-1);for(;;){uint64_t q=tab[p];if(q==std::numeric_limits<uint64_t>::max()){tab[p]=r;return;}if(q==r){auto[it,isnew]=dup.emplace(r,1);uint16_t old=it->second;en+=2ULL*old;it->second=(uint16_t)(old+1);if(it->second>mx){mx=it->second;mxkey=r;}return;}p=(p+1)&(cap-1);}};
  for(auto&q:tr){auto&v=base[(4-q.c)&15];uint64_t st=subm(S0,q.d);circular_slice(v,st,lo,hi,[&](uint64_t b){ins(b,q.d);});if(L2<MOD&&L2<U2)circular_slice(v,st,L2,U2,[&](uint64_t b){ins(b,q.d);});}
  if(acc!=total)throw std::runtime_error("shard count mismatch");entries.fetch_add(acc,std::memory_order_relaxed);energy.fetch_add(en,std::memory_order_relaxed);
  uint16_t old=global_max.load();while(mx>old&&!global_max.compare_exchange_weak(old,mx));if(mx>=global_max.load()){global_key.store(mxkey);global_shard.store(shard);}
  int d=done.fetch_add(1)+1;if((d&255)==0||d==SH){std::lock_guard<std::mutex>lk(outmu);std::cerr<<"progress "<<d<<"/"<<SH<<" entries="<<entries.load()<<" energy="<<energy.load()<<" max="<<global_max.load()<<"\n";}
 };
 auto wall3=std::chrono::steady_clock::now();
 #pragma omp parallel for schedule(dynamic,1) num_threads(THREADS)
 for(int s=0;s<SH;s++)process_shard(s);
 auto wall4=std::chrono::steady_clock::now();
 uint64_t got=entries.load(),E=energy.load();uint16_t mx=global_max.load();uint64_t fixed_full_max=2*std::max(fixed0,fixed1);uint64_t projected_max=std::max<uint64_t>(mx,fixed_full_max);
 bool pass=(got==expected&&fixed0==0&&fixed1==0&&projected_max<=12&&E<=154);
 auto sec=[](auto a,auto b){return std::chrono::duration<double>(b-a).count();};
 std::cout<<"{\n"
  <<"  \"decision\": \""<<(pass?"TAU_FOLDED_PROJECTED_MMAX_LE_12":"TAU_FOLDED_PROJECTED_CHECK_FAILED")<<"\",\n"
  <<"  \"projection_modulus\": "<<MOD<<",\n  \"kernel_order\": 3,\n  \"kappa\": "<<KAP<<",\n"
  <<"  \"fixed_roots\": ["<<S0<<", "<<S1<<"],\n  \"fixed_selected_counts\": ["<<fixed0<<", "<<fixed1<<"],\n"
  <<"  \"tau_half_domain_expected\": "<<expected<<",\n  \"tau_half_domain_counted\": "<<got<<",\n"
  <<"  \"canonical_shards\": "<<SH<<",\n  \"threads\": "<<THREADS<<",\n"
  <<"  \"folded_ordered_energy\": "<<E<<",\n  \"max_canonical_projected_multiplicity\": "<<mx<<",\n"
  <<"  \"max_canonical_key\": "<<global_key.load()<<",\n  \"max_key_shard\": "<<global_shard.load()<<",\n"
  <<"  \"full_projected_max_including_fixed\": "<<projected_max<<",\n"
  <<"  \"thresholds\": {\"energy_pass_max\": 154, \"multiplicity_pass_max\": 12},\n"
  <<"  \"seconds\": {\"generate_base\": "<<sec(wall0,wall1)<<", \"sort_and_check_base\": "<<sec(wall1,wall2)<<", \"setup\": "<<sec(wall2,wall3)<<", \"shard_scan\": "<<sec(wall3,wall4)<<", \"total\": "<<sec(wall0,wall4)<<"}\n}\n";
 return pass?0:1;
}
