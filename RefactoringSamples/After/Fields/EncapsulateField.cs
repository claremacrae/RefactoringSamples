namespace RefactoringSamples.After.Fields
{
    // begin-snippet: EncapsulateField-After
    public class EncapsulateField
    {
        public int Thing1AsAutoProperty { get; }

        public int Thing2
        {
            get => _thing2;
            set => _thing2 = value;
        }

        private int _thing2;
    }
    // end-snippet
}