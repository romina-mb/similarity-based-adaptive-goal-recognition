import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class ReLearnController {

	public static void main(String[] args) throws IOException {
		// based on number of traces (10 traces to re-learn)
		
		
		// parameters
		// 2 ../recognizer/Feedback/Add 
		
		int error_collection_threshold = Integer.parseInt(args[0]);
		
		// the location of re-learned plans
		// String trace_dir = "../recognizer/Feedback/Add";
		String trace_dir = args[1];
		
		// list of trace_dir
		File file = new File(trace_dir);
		
		for (File planSet : file.listFiles()) {
			// number of collected plan for re-learn
			
			
			if (!planSet.isHidden()) {
				int collected = planSet.list().length;
				
				//System.out.println("Working Directory = " + System.getProperty("user.dir"));
				if (collected >= error_collection_threshold) {
					System.out.println("Yes: need to relearn : model " + planSet.getName());
					generateXES(planSet.getPath(), "model" + planSet.getName() + ".xes");
					
					// delete collected traces
					deleteDirectoryRecursion(planSet);
					
				} else {
					System.out.println("No, keep collecting");
				}
			}
		}
		
		
		
		
		
		// parameters:
		// ../recognizer/Feedback/Add 0.6 0.8
		
		// String trace_dir = "../recognizer/Feedback/Add";
		
		/*
		String trace_dir = args[0];
		
		
		double currentAcc = Double.parseDouble(args[1]);
		// re-learn trigger
		double accThreshold = Double.parseDouble(args[2]);
		
		
		if (currentAcc < accThreshold) {
			File file = new File(trace_dir);
			
			for (File planSet : file.listFiles()) {
				if (!planSet.isHidden()) {
					System.out.println("Yes: need to relearn : model " + planSet.getName());
					generateXES(planSet.getPath(), "model" + planSet.getName() + ".xes");
					
					// delete collected traces
					// deleteDirectoryRecursion(planSet);
				}
			}
			
		}
		*/

	}
	
	
	// based on what to re-learn
	// 1. learn from new observations (re-mine the model, provide XES files for goals)
	public static void generateXES(String directory, String output) throws IOException {
		
		File folder = new File(directory);
		File[] listOfFiles = folder.listFiles();
		
		String head = "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\r\n" + 
		"<log xes.version=\"1.0\" xes.features=\"nested-attributes\" openxes.version=\"1.0RC7\" " +
		"xmlns=\"http://www.xes-standard.org/\">\n";
		
		String tail = "</log>";
		
		File newTextFile = new File(output);
        FileWriter fw = new FileWriter(newTextFile);
        fw.write(head);

		for (File file : listOfFiles) {
		    if (file.isFile()) {
		    	fw.write("<trace>\n");
		        BufferedReader br = new BufferedReader(new FileReader(file));
		        String st;
		        while ((st = br.readLine()) != null) {
		        	char firstChar = st.charAt(0);
		        	if (firstChar != ';') {
		        		fw.write("<event>\n");
			        	fw.write("<string key=\"concept:name\" value=\""+ st + "\"/>" + "\n");
			        	fw.write("</event>\n");
		        	} 
		        }
		        fw.write("</trace>\n");
		        br.close();
		    }
		}
		
		fw.write(tail);
		fw.close();
	}
	
	
	
	
	
	public static void deleteDirectoryRecursion(File file) throws IOException {
		if (file.isDirectory()) {
			File[] entries = file.listFiles();
		    if (entries != null) {
		    	for (File entry : entries) {
		    		deleteDirectoryRecursion(entry);
		    	}
		    }
		}
		if (!file.delete()) {
			throw new IOException("Failed to delete " + file);
		}
	}
	
	
}
