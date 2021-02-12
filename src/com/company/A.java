package com.company;

import java.util.Arrays;

public class A {




    public String removeDuplicate(char str[], int n){

        int index = 0;

        for (int i = 0; i < n; i++)
        {

            int j;
            for(j = 0; j < i; j++){

                if(str[i] == str[j]){
                    break;
                }
            }

            if(j == i){
                str[index++] = str[j];

            }


        }

        return String.valueOf(Arrays.copyOf(str, index));
    };

}
