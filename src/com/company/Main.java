package com.company;

import com.company.carpet.Calculator;
import com.company.carpet.Carpet;
import com.company.carpet.Floor;
import com.company.test.Point;
import com.company.test.Wall;

public class Main {

    public static void main(String[] args) {

        Wall wall = new Wall(5, 4);
//        System.out.println("area= " + wall.getArea());
//
//        wall.setHeight(-1.5);
//        System.out.println("width= " + wall.getWidth());
//        System.out.println("height= " + wall.getHeight());
//        System.out.println("area= " + wall.getArea());

//        Point first = new Point(6, 5);
//        Point second = new Point(3, 1);
//        System.out.println("distance(0,0)= " + first.distance());
//        System.out.println("distance(second)= " + first.distance(second));
//        System.out.println("distance(2,2)= " + first.distance(2, 2));
//        Point point = new Point();
//        System.out.println("distance()= " + point.distance());


//        Carpet carpet = new Carpet(3.5);
//        Floor floor = new Floor(2.75, 4.0);
//        Calculator calculator = new Calculator(floor, carpet);
//        System.out.println("total= " + calculator.getTotalCost());
//        carpet = new Carpet(1.5);
//        floor = new Floor(5.4, 4.5);
//        calculator = new Calculator(floor, carpet);
//        String s = Integer.toString(100, 2);
//        int count = 0;
//        for (int i = 0; i < s.length(); i++){
//            if(Integer.parseInt(String.valueOf(s.charAt(i))) == 1){
//                count++;
//                if()
//
//            }
//        }
//        System.out.println("total= " + calculator.getTotalCost());

        A a = new A();
        String str = "OBsS Coding Interview";
        char[] chars = str.toCharArray();
        int len = str.length();

        a.removeDuplicate(chars, len);
        System.out.println("result :" + a.removeDuplicate(chars, len));
    }
}
