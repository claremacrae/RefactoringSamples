namespace RefactoringSamples.Keys
{
    public class Key
    {
        public int PublicField = 0;
        public static int PublicFieldStatic = 0;

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