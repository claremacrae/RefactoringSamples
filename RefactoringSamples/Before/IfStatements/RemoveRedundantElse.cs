using System;

namespace RefactoringSamples.Before.IfStatements
{
    public class RemoveRedundantElse
    {
        public string HeavilyNestedIf()
        {
            if ((new Random().Next() % 3) == 0)
            {
                return "Multiple of 3";
            }
            else
            {
                if ((new Random().Next() % 4) == 0)
                {
                    return "Multiple of 4";
                }
                else
                {
                    if ((new Random().Next() % 5) == 0)
                    {
                        return "Multiple of 5";
                    }
                }
            }

            return "Value not recognised";
        }
    }
}