import java.io.File;
import java.io.IOException;

public class OpenLoop extends RelearnMethodTemplate {
	
	//////// need to be careful with the name prefix, here we use "goal_"
	
	int error_collection_threshold;
	String trace_dir;
	
	// constructor
	public OpenLoop(int error_collection_threshold, String trace_dir) {
		this.error_collection_threshold = error_collection_threshold;
		
		// the location of re-learned plans
		this.trace_dir = trace_dir;   //"../recognizer/Feedback/Add";
	}
	

	public void checkAndRelearn() throws IOException {
		
		// list of trace_dir
		File file = new File(trace_dir);
		
		for (File planSet : file.listFiles()) {
			// number of collected plan for re-learn
			
			
			if (!planSet.isHidden()) {
				int collected = planSet.list().length;
				
				//System.out.println("Working Directory = " + System.getProperty("user.dir"));
				if (collected >= error_collection_threshold) {
					System.out.println("Yes: need to relearn : goal_" + planSet.getName());
					generateXES(planSet.getPath(), "goal_" + planSet.getName() + ".xes");
					
					// delete collected traces
					deleteDirectoryRecursion(planSet);
					
				} else {
					System.out.println("No, keep collecting");
				}
			}
		}
		
	}
	
	
	

}
