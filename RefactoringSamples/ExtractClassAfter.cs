namespace RefactoringSamples
{
    public class Concept2
    {
        private int _concept2;

        public int Concept2Function()
        {
            return _concept2;
        }
    }

    public class Concept1
    {
        private int _concept1;

        public int Concept1Function()
        {
            return _concept1;
        }
    }

    public class ExtractClassAfter
    {
        private readonly Concept1 _concept1 = new Concept1();
        private readonly Concept2 _concept2 = new Concept2();
    }
}