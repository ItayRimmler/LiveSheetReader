#include <vector>
#include <string>
#include "../all/Note.h"
using namespace std;

class Chain{
    private:
        //Member variables:
        vector<Note> val;
        vector<int> cont;
        double score;
        int page_num;
        //Private methods:
    public:
        //Getters:
        vector<Note> get_val() const {return val;};
        vector<int> get_cont() const {return cont;};
        double get_score() const {return score;};
        int get_page_num() const {return page_num;};
        //Setters:
        void set_val(const vector<Note>& other) {val = other;};
        void set_score(const double& other) {score = other;};
        void set_page_num(const int& other) {page_num = other;};
        //Constructors:
        Chain(){val.push_back(Note()); cont = calc_cont(); score = calc_score(); page_num = 0;};
        Chain(const vector<Note>& notes) : val(notes) {cont = calc_cont(); score = calc_score(); page_num = 0;};
        Chain(const vector<Note>& notes, const int& pageNum) : val(notes), page_num(pageNum) {cont = calc_cont(); score = calc_score();};
        Chain(const int& pageNum) : page_num(pageNum) {val.push_back(Note()); cont = calc_cont(); score = calc_score();};
        //Operators:
        Chain operator+()
        //Methods:
        vector<int> get_groups() const;
        vector<int> get_indices() const;
        vector<string> get_types() const;
        void calc_score() const;
        void calc_cont() const;
}