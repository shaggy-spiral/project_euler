using System;

namespace euler
{
    class Program
    {
        static void Main(string[] args) {
            int limit = (int)Math.Sqrt(1000);
            double a, b, c, powa, powb, powc = 0;
            

            for(a = 1; a < 995; a++) {
                for(b = 2; b < 996; b++) {
                    for(c = 3; c < 997; c++) {
                        powa = Math.Pow(a, 2);
                        powb = Math.Pow(b, 2);
                        powc = Math.Pow(c, 2);     
                        if ((powa + powb) == powc) {
                            if (a + b + c == 1000) {
                                Console.WriteLine("Triplet! A: " + a + ", B: " + b + ", C: " + c);
                            }
                        }
                    }
                }
            }
            Console.WriteLine(":(");
        }
    }
}