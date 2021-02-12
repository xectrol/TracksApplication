package com.company.patterns.creational.abstractfactory;

public class HDFC implements Bank {

    private String BName;

    public HDFC(){
        BName = "HDFC BANK";
    }

    @Override
    public String getBankName() {
        return BName;
    }
}
