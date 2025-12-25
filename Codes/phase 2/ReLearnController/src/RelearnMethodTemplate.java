import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

// this is a superclass
public class RelearnMethodTemplate {
	
	// public void checkAndRelearn();
	
	// based on what to re-learn
	// 1. learn from new observations (re-mine the model, provide XES files for goals)
	public void generateXES(String directory, String output) throws IOException {
		
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
	
	
	public void deleteDirectoryRecursion(File file) throws IOException {
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
