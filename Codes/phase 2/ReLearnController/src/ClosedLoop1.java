import java.io.File;
import java.io.IOException;

public class ClosedLoop1 extends RelearnMethodTemplate {
	
	String trace_dir;
	// re-learn trigger
	double currentAcc;
	double accThreshold;
	
	
	// constructor
	public ClosedLoop1(String trace_dir, double currentAcc, double accThreshold) {
		// the location of re-learned plans
		this.trace_dir = trace_dir;   //"../recognizer/Feedback/Add";
		this.currentAcc = currentAcc;
		this.accThreshold = accThreshold;
	}
	
	
	public void checkAndRelearn() throws IOException {
		if (currentAcc < accThreshold) {
			File file = new File(trace_dir);
			
			for (File planSet : file.listFiles()) {
				if (!planSet.isHidden()) {
					System.out.println("Yes: need to relearn : goal_" + planSet.getName());
					generateXES(planSet.getPath(), "goal_" + planSet.getName() + ".xes");
					
					// delete collected traces
					// deleteDirectoryRecursion(planSet);
				}
			}
			
		}
	}
	


}
