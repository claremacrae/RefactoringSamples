﻿namespace RefactoringSamples
{
    public class ExtractClassBefore
    {
        private int _concept1;
        private int _concept2;

        public int Concept1Function()
        {
            return _concept1;
        }
        
        public int Concept2Function()
        {
            return _concept2;
        }
    }
}