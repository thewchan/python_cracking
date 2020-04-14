import java.util.*;

public class AscendingTrend {

    public static void main(String[] args) {
        
        if (args.length < 1) {
            System.out.println("This program needs exactly one argument: INT_STRING");
            System.exit(1);
        }
        String intString = args[0];
        ArrayList<String> strSegments = new ArrayList<String>();
        int segmentIndex = 0;
        
        for (int i = 0; i < intString.length(); i++) {
            strSegments.add("");
        }
        strSegments.set(segmentIndex, strSegments.get(segmentIndex) + intString.charAt(0));
        int counter = 1;

        for (int j = 0; j < intString.length(); j++) {
            if (counter == intString.length()) {
                break;
            }
            counter++;

            if ((int) intString.charAt(j) < (int) intString.charAt(j+1)) {
                strSegments.set(segmentIndex, strSegments.get(segmentIndex) + intString.charAt(j+1));
            } else {
                segmentIndex++;
                strSegments.set(segmentIndex, strSegments.get(segmentIndex) + intString.charAt(j+1));
            }
        }

        String longest = strSegments.get(0);

        for (String segment : strSegments) {
            if (segment.length() > longest.length()) {
                longest = segment;
            }
        }

        int strLength = longest.length();
        int sum = 0;

        for (int k = 0; k < strLength; k++) {
            sum += (int) longest.charAt(k);
        }

        float average = (float) sum / (float) strLength;

        System.out.println(String.format("Longest substring in numeric ascending order is: %s Average: %.2f", longest, average));


    }
}