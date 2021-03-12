namespace RefactoringSamples
{
    public class ExtractFieldBefore
    {
        public void LongMethod()
        {
            int thing1;
            int thing2;
            int thing3;
        }
    }

    public class ExtractFieldAfter
    {
        private int _thing1;
        private int _thing2;
        private int _thing3;

        public void LongMethod()
        {
        }
    }
}
