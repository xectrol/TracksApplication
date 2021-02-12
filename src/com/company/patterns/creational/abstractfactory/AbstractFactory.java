package com.company.patterns.creational.abstractfactory;

public abstract class AbstractFactory {

    public abstract Bank getBank(String bank);
    public abstract Loan getLoan(String loan);

    public void a() {

    }
}
