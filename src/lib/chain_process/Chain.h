#pragma once
#include <vector>
#include <string>
#include "C:/Users/User/PycharmProjects/LiveSheetReader/ver2/src/lib/all/Note.h"
using namespace std;

class Chain{
    private:
        //Member variables:
        vector<Note> val;
        vector<int> cont;
        double score;
        int page_num;
        //Private methods:
        vector<Chain> possible_matches(const vector<Note>& other) const;
    public:
        //Getters:
        vector<Note> get_val() const {return this->val;};
        vector<int> get_cont() const {return this->cont;};
        double get_score() const {return this->score;};
        int get_page_num() const {return this->page_num;};
        int get_len() const {return static_cast<int>(this->val.size());};
        //Setters:
        void set_val(const vector<Note>& other) {this->val = other;};
        void set_score(const double& other) {this->score = other;};
        void set_page_num(const int& other) {this->page_num = other;};
        //Constructors:
        Chain(){val.push_back(Note()); this->calc_cont(); this->calc_score(); this->page_num = 1;};
        Chain(const Chain& other) {this->val = other.get_val(); this->page_num = other.get_page_num(); this->calc_cont(); this->calc_score();};
        Chain(const vector<Note>& notes) : val(notes) {this->calc_cont(); this->calc_score(); this->page_num = 1;};
        Chain(const vector<Note>& notes, const int& pageNum) : val(notes), page_num(pageNum) {this->calc_cont(); this->calc_score();};
        Chain(const int& pageNum) : page_num(pageNum) {this->val.push_back(Note()); this->calc_cont(); this->calc_score();};
        //Operators:
        Chain operator+(const vector<Note>& other) {this->val.insert(this->val.end(), other.begin(), other.end()); return Chain(this->val);};
        //Methods:
        vector<int> get_groups() const;
        vector<int> get_indices() const;
        vector<string> get_types() const;
        void calc_score();
        void calc_cont();
        vector<Note> match(const vector<Note>& other) const;
};