#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>
#include "logsM.hpp"
#include "logsN.hpp"

static constexpr uint64_t KAP=15337197211725320908ULL;
static constexpr uint64_t S0=7668598605862660454ULL;
static constexpr __uint128_t N=(__uint128_t)4866119187566686848ULL*10;
static constexpr __uint128_t M128=(__uint128_t)MOD;

static constexpr uint64_t DUP_KEYS[30]={
179351812256751797ULL,179795084433593580ULL,222915557520769006ULL,
254958237482354612ULL,1871222699767544580ULL,1946829124993147395ULL,
2115829786642026153ULL,2191436211867628968ULL,2752876908959724607ULL,
3173541850524071265ULL,3275293692624999094ULL,3807700674152818936ULL,
3834149319236634720ULL,3861193039733633404ULL,3883307099378421751ULL,
3909755744462237535ULL,4992786929752216345ULL,5035907402839391771ULL,
5526020206747427503ULL,5601626631973030318ULL,5770627293621909076ULL,
5846233718847511891ULL,6514369406671509109ULL,6616121248772436938ULL,
6733442005186036094ULL,6835193847286963923ULL,7462498181132701859ULL,
7538104606358304674ULL,7546212406836699991ULL,7565868754278347372ULL};

static inline uint64_t addm(uint64_t a,uint64_t b){
    __uint128_t z=(__uint128_t)a+b;
    if(z>=MOD) z-=MOD;
    return (uint64_t)z;
}
static inline uint64_t subm(uint64_t a,uint64_t b){
    return a>=b?a-b:(uint64_t)((__uint128_t)a+MOD-b);
}
static inline __uint128_t addn(__uint128_t a,__uint128_t b){
    __uint128_t z=a+b;
    if(z>=N) z-=N;
    return z;
}
static inline __uint128_t logn(int t,int k){
    return ((__uint128_t)LOGN_HI[t][k]<<64) | (__uint128_t)LOGN_LO[t][k];
}
static int tauk(int k){
    int i=k/16+1,a=k%16;
    if(i==1) return 16+(a+6)%16;
    if(i==2) return (a+10)%16;
    return 32+(a+8)%16;
}
static std::string u128s(__uint128_t x){
    if(x==0) return "0";
    std::string s;
    while(x){ s.push_back(char('0'+x%10)); x/=10; }
    std::reverse(s.begin(),s.end());
    return s;
}

struct Key{
    uint64_t sum;
    uint8_t color;
    bool operator==(const Key&o)const{return sum==o.sum&&color==o.color;}
};
struct KeyHash{
    size_t operator()(const Key&k)const noexcept{
        uint64_t x=k.sum + 0x9e3779b97f4a7c15ULL + ((uint64_t)k.color<<56);
        x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL;
        x=(x^(x>>27))*0x94d049bb133111ebULL;
        return (size_t)(x^(x>>31));
    }
};
struct Candidate{
    uint8_t dup, side, k6, k7;
    uint64_t target_base, target_full;
    uint8_t color;
};
struct Witness{
    uint8_t dup,side;
    std::array<uint8_t,7> selected;
    std::array<uint8_t,7> normalized;
    uint64_t projected_selected;
    __uint128_t full_normalized;
};

static uint64_t projected_sum(const std::array<uint8_t,7>&x){
    uint64_t s=0; for(int t=0;t<7;t++) s=addm(s,LOGS[t][x[t]]); return s;
}
static __uint128_t full_sum(const std::array<uint8_t,7>&x){
    __uint128_t s=0; for(int t=0;t<7;t++) s=addn(s,logn(t,x[t])); return s;
}
static int color_sum(const std::array<uint8_t,7>&x){
    int s=0;for(int t=0;t<7;t++)s=(s+COLORS[t][x[t]])&15;return s;
}
static void print_tuple(const std::array<uint8_t,7>&x){
    std::cout<<"[";
    for(int t=0;t<7;t++){if(t)std::cout<<", ";std::cout<<(int)x[t];}
    std::cout<<"]";
}

int main(){
    // Header-to-field-log chain sanity: full logs reduce to the projected table.
    if(ORDER!=N || N!=3*M128) throw std::runtime_error("order mismatch");
    for(int t=0;t<7;t++)for(int k=0;k<48;k++){
        if(logn(t,k)>=N || (uint64_t)(logn(t,k)%M128)!=LOGS[t][k])
            throw std::runtime_error("full/projected log mismatch");
    }
    std::vector<int> H;
    for(int k=0;k<48;k++){
        if(tauk(tauk(k))!=k || tauk(k)==k) throw std::runtime_error("tau failure");
        if(k<tauk(k)) H.push_back(k);
    }
    if(H.size()!=24) throw std::runtime_error("orientation failure");

    std::vector<Candidate> cand;
    cand.reserve(30*2*48*48);
    std::unordered_map<Key,std::vector<uint32_t>,KeyHash> want;
    want.reserve(180000);
    for(uint8_t j=0;j<30;j++){
        uint64_t r=DUP_KEYS[j];
        uint64_t xs[2]={addm(S0,r),subm(S0,r)};
        for(uint8_t side=0;side<2;side++)for(uint8_t k6=0;k6<48;k6++)for(uint8_t k7=0;k7<48;k7++){
            uint64_t d=addm(LOGS[5][k6],LOGS[6][k7]);
            uint8_t cq=(COLORS[5][k6]+COLORS[6][k7])&15;
            uint8_t cb=(4-cq)&15;
            uint64_t b=subm(xs[side],d);
            uint32_t idx=(uint32_t)cand.size();
            cand.push_back({j,side,k6,k7,b,xs[side],cb});
            want[{b,cb}].push_back(idx);
        }
    }
    if(cand.size()!=138240) throw std::runtime_error("candidate count");

    std::vector<Witness> wit;
    wit.reserve(80);
    uint64_t base_count=0;
    for(int k1:H)for(int k2=0;k2<48;k2++)for(int k3=0;k3<48;k3++){
        uint64_t s3=addm(addm(LOGS[0][k1],LOGS[1][k2]),LOGS[2][k3]);
        int c3=(COLORS[0][k1]+COLORS[1][k2]+COLORS[2][k3])&15;
        for(int k4=0;k4<48;k4++){
            uint64_t s4=addm(s3,LOGS[3][k4]);
            int c4=(c3+COLORS[3][k4])&15;
            for(int k5=0;k5<48;k5++){
                uint64_t b=addm(s4,LOGS[4][k5]);
                uint8_t cb=(c4+COLORS[4][k5])&15;
                base_count++;
                auto it=want.find({b,cb});
                if(it==want.end()) continue;
                for(uint32_t ci:it->second){
                    const Candidate&q=cand[ci];
                    std::array<uint8_t,7> x={(uint8_t)k1,(uint8_t)k2,(uint8_t)k3,(uint8_t)k4,(uint8_t)k5,q.k6,q.k7};
                    if(color_sum(x)!=4 || projected_sum(x)!=q.target_full) throw std::runtime_error("witness target mismatch");
                    uint64_t z=subm(q.target_full,S0), rr=std::min(z,MOD-z);
                    if(rr!=DUP_KEYS[q.dup]) throw std::runtime_error("canonical mismatch");
                    std::array<uint8_t,7> y=x;
                    if(q.side==1) for(int t=0;t<7;t++) y[t]=(uint8_t)tauk(y[t]);
                    if(projected_sum(y)!=addm(S0,DUP_KEYS[q.dup]) || color_sum(y)!=4) throw std::runtime_error("normalization mismatch");
                    wit.push_back({q.dup,q.side,x,y,q.target_full,full_sum(y)});
                }
            }
        }
    }
    if(base_count!=127401984ULL) throw std::runtime_error("base count mismatch");

    std::array<std::vector<Witness>,30> by;
    for(auto&w:wit) by[w.dup].push_back(w);
    uint64_t true_orbits=0;
    for(int j=0;j<30;j++){
        if(by[j].size()!=2) throw std::runtime_error("duplicate lift count is not two");
        if(by[j][0].normalized==by[j][1].normalized) throw std::runtime_error("same normalized tuple twice");
        __uint128_t a=by[j][0].full_normalized,b=by[j][1].full_normalized;
        __uint128_t diff=a>=b?a-b:a+N-b;
        if(diff%M128) throw std::runtime_error("kernel difference mismatch");
        unsigned q=(unsigned)(diff/M128);
        if(q>2) throw std::runtime_error("kernel quotient");
        if(q==0) true_orbits++;
    }
    uint64_t true_double_fibers=2*true_orbits;
    uint64_t true_D=2*true_double_fibers;
    uint64_t p0=52747567104ULL;
    uint64_t occupancy=p0-true_double_fibers;
    unsigned exact_mmax=true_orbits?2:1;

    std::cout<<"{\n";
    std::cout<<"  \"decision\": \"KERNEL_3_DUPLICATE_LIFT_COMPLETE\",\n";
    std::cout<<"  \"projection_modulus\": "<<MOD<<",\n";
    std::cout<<"  \"projection_duplicate_orbits_checked\": 30,\n";
    std::cout<<"  \"candidate_base_targets\": "<<cand.size()<<",\n";
    std::cout<<"  \"oriented_five_slot_tuples_scanned\": "<<base_count<<",\n";
    std::cout<<"  \"selected_witnesses_recovered\": "<<wit.size()<<",\n";
    std::cout<<"  \"true_collision_tau_orbits\": "<<true_orbits<<",\n";
    std::cout<<"  \"true_double_fibers\": "<<true_double_fibers<<",\n";
    std::cout<<"  \"exact_true_ordered_offdiagonal_energy\": "<<true_D<<",\n";
    std::cout<<"  \"exact_true_m_max\": "<<exact_mmax<<",\n";
    std::cout<<"  \"exact_true_occupancy\": "<<occupancy<<",\n";
    std::cout<<"  \"lifts\": [\n";
    for(int j=0;j<30;j++){
        auto&A=by[j][0];auto&B=by[j][1];
        __uint128_t diff=A.full_normalized>=B.full_normalized?A.full_normalized-B.full_normalized:A.full_normalized+N-B.full_normalized;
        unsigned q=(unsigned)(diff/M128);
        std::cout<<"    {\"canonical_key\": "<<DUP_KEYS[j]<<", \"kernel_difference\": "<<q<<", \"true_collision\": "<<(q==0?"true":"false")<<", \"witnesses\": [";
        Witness* ws[2]={&A,&B};
        for(int z=0;z<2;z++){
            if(z)std::cout<<", ";
            std::cout<<"{\"selected_side\": "<<(int)ws[z]->side<<", \"selected_tuple\": ";print_tuple(ws[z]->selected);
            std::cout<<", \"normalized_tuple\": ";print_tuple(ws[z]->normalized);
            std::cout<<", \"normalized_full_log\": \""<<u128s(ws[z]->full_normalized)<<"\"}";
        }
        std::cout<<"]}"<<(j==29?"":",")<<"\n";
    }
    std::cout<<"  ]\n}\n";
    return 0;
}
