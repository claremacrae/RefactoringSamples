namespace RefactoringSamples.Keys
{
    public class Key2
    {
        public static int StaticPublicField = 0;
        public int PublicField = 0;

        protected static int StaticProtectedField = 0;
        protected int ProtectedField = 0;

        private static int _staticPrivateField = 0;
        private int _privateField = 0;

        public int PublicMethod()
        {
            return PublicField;
        }

        public static int StaticPublicMethod()
        {
            return StaticPublicField;
        }

        protected static int StaticProtectedMethod()
        {
            return StaticProtectedField;
        }

        protected int ProtectedMethod()
        {
            return ProtectedField;
        }

        private int PrivateMethod()
        {
            return _privateField;
        }

        private static int StaticPrivateMethod()
        {
            return _staticPrivateField;
        }
    }
}