

int s_id = 1, p_id = 1;

class Person{
    public:
        string members;
        int age;
        virtual void getdata(){};
        virtual void putdata(){};
};

class Professor: public Person{
    public:
        int publications,cur_id = p_id++;
        void getdata(){
            cin >> members >>age >> publications;
        };
        void putdata(){
            cout << members << " " << age << " "  << publications << " "  << cur_id << endl;
        }
};
class Student: public Person{
    public:
        int marks[6], cur_id = s_id++;
        void getdata(){
            cin >> members >>age;
            for (int i = 0; i<6;++i){
                cin >> marks[i];
            }
        };
        void putdata(){
            int suma = 0;
            for (int i = 0; i<6;++i){
                suma += marks[i];
            }
            cout << members << " "  << age << " "  << suma << " "  << cur_id << endl;
        }
};
