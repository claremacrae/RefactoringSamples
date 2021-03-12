namespace RefactoringSamples.Extract.After
{
    public interface IExtractInterfaceAfter
    {
        int method1();
        int method2();
    }

    public class ExtractInterface : IExtractInterfaceAfter
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
}