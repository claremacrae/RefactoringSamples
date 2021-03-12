﻿namespace RefactoringSamples.After.Extract
{
    public interface IExtractInterface
    {
        int method1();
        int method2();
    }

    public class ExtractInterface : IExtractInterface
    {
        public int method1()
        {
            return 0;
        }

        public int method2()
        {
            return 0;
        }
    }
}