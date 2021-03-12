namespace RefactoringSamples.Encapsulate.After
{
    public class EncapsulateFieldAfter
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