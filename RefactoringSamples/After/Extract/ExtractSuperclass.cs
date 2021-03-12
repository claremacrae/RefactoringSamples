namespace RefactoringSamples.After.Extract
{
    public class ExtractSuperclassBase
    {
        private int method1()
        {
            return 0;
        }

        private int method2()
        {
            return 0;
        }
    }

    public class ExtractSuperclass : ExtractSuperclassBase
    {
    }
}