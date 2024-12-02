package org.example;

import java.io.*;
import java.util.*;

public class Main {
/*
3   4
4   3
2   5
1   3
3   9
3   3
 */
    public static void main(String[] args) {
//        List<Integer> list1 = Arrays.asList(3, 4, 2, 1, 3, 3);
//        List<Integer> list2 = Arrays.asList(4, 3, 5, 3, 9, 3);
//        Collections.sort(list1);
//        Collections.sort(list2);
//        similarity(list1,list2);
        process();
    }
    public static void process() {

        String filePath = "input1.txt"; // Replace with your file path

        try (InputStream inputStream = Main.class.getClassLoader().getResourceAsStream(filePath);
             BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream))) {

            String line;
            List<Integer> list1 = new ArrayList<>();
            List<Integer>  list2 = new ArrayList<>();

            while ((line = reader.readLine()) != null) {
                String[] numbers = line.split("\\s+");
                list1.add(Integer.parseInt(numbers[0]));
                list2.add(Integer.parseInt(numbers[1]));
            }

            Collections.sort(list1);
            Collections.sort(list2);
            System.out.println(list1);
            System.out.println(list2);
            compare(list1,list2);
            similarity(list1,list2);

        } catch (Exception e) {
            System.err.println("Error reading the file: " + e.getMessage());
        }


    }

    public static void compare(List<Integer> list1, List<Integer> list2) {
        int diff = 0;
        int sum = 0;
        for (int i = 0; i < list1.size(); i++) {
            diff = Math.abs(list1.get(i) - list2.get(i));
            System.out.println("differnce between "+ list2.get(i) + " and  " +  list1.get(i) + " =" + diff);
            sum = sum + diff;
        }
        System.out.println(sum);
    }
    public static void similarity(List<Integer> list1, List<Integer> list2) {
        int diff = 0;
        int sum = 0;
        for (int i = 0; i < list1.size(); i++) {
            int occurrences = Collections.frequency(list2, list1.get(i));
            sum = sum +  list1.get(i)* occurrences;

        }
        System.out.println(sum);
    }
}