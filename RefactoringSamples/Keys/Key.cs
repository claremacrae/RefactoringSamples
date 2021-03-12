using System;

namespace RefactoringSamples
{
    public class Key
    {
        public static int StaticPublicField = 0;
        public int PublicField = 0;

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