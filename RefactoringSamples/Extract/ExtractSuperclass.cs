﻿namespace RefactoringSamples.Extract
{
    public class ExtractSuperclassAfterBase
    {
        private int method1()
        {
            return 0;
        }

        private int method2()
        {
            return 0;
        }
    }

    public class ExtractSuperclassAfter : ExtractSuperclassAfterBase
    {
    }
}