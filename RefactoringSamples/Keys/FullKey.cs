namespace RefactoringSamples.Keys
{
    public class Key2
    {
        public int PublicField = 0;
        public static int PublicFieldStatic = 0;

        protected int ProtectedField = 0;
        protected static int ProtectedFieldStatic = 0;

        private int _privateField = 0;
        private static int _privateFieldStatic = 0;

        public int PublicMethod()
        {
            return PublicField;
        }

        public static int PublicMethodStatic()
        {
            return PublicFieldStatic;
        }

        protected int ProtectedMethod()
        {
            return ProtectedField;
        }

        protected static int ProtectedMethodStatic()
        {
            return ProtectedFieldStatic;
        }

        private int PrivateMethod()
        {
            return _privateField;
        }

        private static int PrivateMethodStatic()
        {
            return _privateFieldStatic;
        }
    }
}