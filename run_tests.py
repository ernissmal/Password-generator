import unittest
import os
import sys
import logging
import time
from datetime import datetime

# Configure logging for test run
log_filename = f"test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("TestRunner")

def run_all_tests():
    """Run all tests and generate a report."""
    start_time = time.time()
    logger.info("Starting Password Generator Test Suite")
    logger.info(f"Test run started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Discover and run tests
    loader = unittest.TestLoader()
    test_dir = os.path.join(os.path.dirname(__file__), 'tests')
    suite = loader.discover(test_dir)
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Calculate run time
    end_time = time.time()
    run_time = end_time - start_time
    
    # Generate test summary
    logger.info("\n" + "="*60)
    logger.info("TEST SUMMARY")
    logger.info("="*60)
    logger.info(f"Total tests run: {result.testsRun}")
    logger.info(f"Tests passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    logger.info(f"Tests failed: {len(result.failures)}")
    logger.info(f"Tests with errors: {len(result.errors)}")
    logger.info(f"Total test runtime: {run_time:.2f} seconds")
    logger.info(f"Test run completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("="*60)
    
    # Log any failures
    if result.failures:
        logger.info("\nFAILURES:")
        for failure in result.failures:
            logger.info(f"\n{failure[0]}")
            logger.info(f"{failure[1]}")
    
    # Log any errors
    if result.errors:
        logger.info("\nERRORS:")
        for error in result.errors:
            logger.info(f"\n{error[0]}")
            logger.info(f"{error[1]}")
    
    logger.info("\nTest log saved to: " + os.path.abspath(log_filename))
    return result

if __name__ == "__main__":
    result = run_all_tests()
    # Exit with non-zero code if tests failed
    sys.exit(len(result.failures) + len(result.errors))
