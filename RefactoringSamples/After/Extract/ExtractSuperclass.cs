namespace RefactoringSamples.After.Extract
{
    public class ExtractSuperclassBase
    {
        public int method1()
        {
            return 0;
        }

        public int method2()
        {
            return 0;
        }
    }

    public class ExtractSuperclass : ExtractSuperclassBase
    {
    }
}