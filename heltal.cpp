#include <cstdlib>
// Integer class 

class Heltal{
	public:
		Heltal(int);
		int get();
		void set(int);
		int fib(long long int n);
	private:
		int val;
		int h_fib(long long int n);
	};
 
Heltal::Heltal(int n){
	val = n;
	}
 
int Heltal::get(){
	return val;
	}
 
void Heltal::set(int n){
	val = n;
	}
	
int Heltal::fib(long long int n)
{
	return h_fib(n);
	}
int Heltal::h_fib(long long int n)
{
    if (n <= 1)
        return n;
    return fib(n-1) + fib(n-2);
}
 
extern "C"{
	Heltal* Heltal_new(int n) {return new Heltal(n);}
	int Heltal_get(Heltal* heltal) {return heltal->get();}
	void Heltal_set(Heltal* heltal, int n) {heltal->set(n);}
	int Heltal_fib(Heltal* heltal, long long int n) {heltal->fib(n);}
	void Heltal_delete(Heltal* heltal){
		if (heltal){
			delete heltal;
			heltal = nullptr;
			}
		}
	}