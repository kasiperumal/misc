import com.splunk.*;
import org.apache.commons.csv.*;

import java.io.FileReader;
import java.io.Reader;

public class SplunkQueryExample {

    public static void main(String[] args) {
        // Splunk connection details
        String host = "your_splunk_host";
        int port = 8089;
        String username = "your_username";
        String password = "your_password";

        // CSV file path
        String csvFilePath = "path_to_your_csv_file.csv";

        // Create a Service instance and log in
        ServiceArgs loginArgs = new ServiceArgs();
        loginArgs.setUsername(username);
        loginArgs.setPassword(password);
        loginArgs.setHost(host);
        loginArgs.setPort(port);

        Service service = Service.connect(loginArgs);

        try (Reader in = new FileReader(csvFilePath)) {
            Iterable<CSVRecord> records = CSVFormat.DEFAULT.withFirstRecordAsHeader().parse(in);
            for (CSVRecord record : records) {
                String customerNumber = record.get("customer number");
                String startTime = record.get("start time");
                String endTime = record.get("end time");

                // Splunk query with customer number, start time, and end time
                String query = "search index=index1 wf_id=" + customerNumber + " | fields events.event_timestamp events.device.id";
                
                JobArgs jobargs = new JobArgs();
                jobargs.setExecutionMode(JobArgs.ExecutionMode.NORMAL);
                jobargs.setEarliestTime(startTime);
                jobargs.setLatestTime(endTime);
                jobargs.setTimeZone("PST"); // Set timezone to PST

                Job job = service.getJobs().create(query, jobargs);

                // Wait for the job to finish
                while (!job.isDone()) {
                    try {
                        Thread.sleep(500);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }

                // Display results for this customer number
                System.out.println("Results for customer number: " + customerNumber);
                for (Event event : job.getResults()) {
                    System.out.println(event.toString());
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
