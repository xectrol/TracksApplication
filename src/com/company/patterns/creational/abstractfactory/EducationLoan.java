package com.company.patterns.creational.abstractfactory;

public class EducationLoan extends Loan {
    @Override
    void getInterestRate(double r) {
        rate = r;
    }
}
