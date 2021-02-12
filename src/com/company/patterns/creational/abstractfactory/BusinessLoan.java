package com.company.patterns.creational.abstractfactory;

public class BusinessLoan extends Loan {
    @Override
    void getInterestRate(double r) {
        rate = r;
    }
}
