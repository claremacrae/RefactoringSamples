namespace RefactoringSamples
{
    public class ExtractSuperclassBefore
    {
        int method1()
        {
            return 0;
        }
        
        int method2()
        {
            return 0;
        }
    }

    public class ExtractSuperclassAfterBase
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

    public class ExtractSuperclassAfter : ExtractSuperclassAfterBase
    {
    }
}