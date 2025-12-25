import java.io.IOException;

public class Controller {

	public static void main(String[] args) throws IOException {
		
		// To call which system:
		// String system = "-openloop";
		String system = args[0];
		switch (system) {
		  case "-openloop":
		    System.out.println("Using " + system);
		    
		    // param: -openloop ../Feedback/Add 2
		    
		    String trace_dir = args[1];
		    int error_collection_threshold = Integer.parseInt(args[2]);
		    OpenLoop openLoopSystem = new OpenLoop(error_collection_threshold, trace_dir);
		    openLoopSystem.checkAndRelearn();
		    
		    break;
		  case "-closedloop_ave_metric":
		    System.out.println("Using " + system);
		    
		    // param: -closedloop_ave_metric ../recognizer/Feedback/Add 0.6 0.8
		    
		    trace_dir = args[1];
		    double currentAcc = Double.parseDouble(args[2]);
		    double accThreshold = Double.parseDouble(args[3]);
		    ClosedLoop1 closedLoopSystem1 = new ClosedLoop1(trace_dir, currentAcc, accThreshold);
		    closedLoopSystem1.checkAndRelearn();
		    break;
		  case "-closedloop_trend":
		    System.out.println("Using " + system);
		    break;
		  case "-closedloop_rl":
		    System.out.println("Using " + system);
		    break;
		}
		

	}

}
