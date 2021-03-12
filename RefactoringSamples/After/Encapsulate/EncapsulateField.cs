namespace RefactoringSamples.Encapsulate.After
{
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
}