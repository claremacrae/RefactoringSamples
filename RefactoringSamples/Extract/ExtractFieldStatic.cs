namespace RefactoringSamples.Extract
{
    public class ExtractFieldStaticBefore
    {
        public static void LongMethod()
        {
            int thing1;
            int thing2;
            int thing3;
        }
    }

    public class ExtractFieldStaticAfter
    {
        private static int _thing1;
        private static int _thing2;
        private static int _thing3;

        public static void LongMethod()
        {
        }
    }
}
