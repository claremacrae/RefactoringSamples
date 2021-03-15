namespace RefactoringSamples.After.Extract
{
    // begin-snippet: ExtractInterface-After
    public interface IExtractInterface
    {
        public int method1();
        public int method2();
    }

    public class ExtractInterface : IExtractInterface
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
    // end-snippet
}