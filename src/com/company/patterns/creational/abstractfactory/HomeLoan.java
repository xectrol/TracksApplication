package com.company.patterns.creational.abstractfactory;

public class HomeLoan extends Loan {

    @Override
    void getInterestRate(double r) {
        rate = r;
    }

}
