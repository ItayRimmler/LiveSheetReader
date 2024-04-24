#pragma once
#include <string>

using namespace std;

class Note {
private:
    int group;
    int index;
    string type;
public:
    //Getters:
    int get_group() const { return this->group; };
    int get_index() const { return this->index; };
    string get_type() const { return this->type; };
    //Setters:
    void set_group(const int& other) { this->group = other; };
    void set_index(const int& other) { this->index = other; };
    void set_type(const string& other) { this->type = other; };
    //Constructors:
    Note() {
        this->type = "Do";
        this->group = 0;
        this->index = 0;
    };
    Note(const Note& other){this->type = other.get_type(); this->index = other.get_index(); this->group = other.get_group();}
    Note(const int& grp, const int& idx, const string& t) : group(grp), index(idx), type(t) {};
    Note(const int& grp, const int& idx) : group(grp), index(idx) {
        this->type = "Do";
    };
    Note(const int& grp, const string& t) : group(grp), type(t) {
        this->group = 0;
    };
    Note(const int& grp) : group(grp) {
        this->index = 0;
        this->type = "Do";
    };
    Note(const string& t) : type(t) {
        this->group = 0;
        this->index = 0;
    };
};
