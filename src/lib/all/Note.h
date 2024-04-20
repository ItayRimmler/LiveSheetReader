#include <string>

using namespace std;

class Note{
    private:
        int group;
        int index;
        string type;
    public:
        //Getters:
        int get_group() const {return group};
        int get_index() const {return index};
        string get_type() const {return type};
        //Setters:
        void set_group(const int& other) {group = other;};
        void set_index(const int& other) {index = other;};
        void set_type(const string& other) {type = other;};
        //Constructors:
        Note();
        Note(const int& grp, const int& idx, const string& t) : group(grp), index(idx), type(t) {}
        Note(const int& grp, const int& idx) : group(grp), index(idx) {
            type = "Do";
       }
        Note(const int& grp, const string& t) : group(grp), type(t) {
            index = 0;
        }
        Note(const int& idx, const string& t) : index(idx), type(t) {
            group = 0;
        }
        Note(const int& grp) : group(grp) {
            index = 0;
            type = "Do";
        }
        Note(const int& idx) : index(idx) {
            group = 0;
            type = "Do";
        }
        Note(const string& t) : type(t) {
            group = 0;
            index = 0;
        }
}