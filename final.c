#include <Servo.h>
#include <math.h>

const int MIC_THRESHOLD = 700;  // Threshold for detecting a voice
const int RECORDING_DURATION = 1;  // Duration of the recording in seconds
const int NUM_SAMPLES = 30;  // Number of samples to record
const int SAMPLING_RATE = 50;  // Sampling rate of the recording in Hz
const int NUM_CHANNELS = 1;  // Number of channels (1 for mono, 2 for stereo)
const int BIT_DEPTH = 16;  // Bit depth of the recording (8, 16, 24, or 32)

Servo servo;  // Servo motor

int mic1_pin = A0;  // Pin for microphone 1
int mic2_pin = A2;  // Pin for microphone 2
int mic3_pin = A1;  // Pin for microphone 3

int mic1_levels[NUM_SAMPLES];  // Array for storing the power levels of microphone 1
int mic2_levels[NUM_SAMPLES];  // Array for storing the power levels of microphone 2
int mic3_levels[NUM_SAMPLES];  // Array for storing the power levels of microphone 3

void setup() {
  Serial.begin(9600);
  // Set up the servo motor
  servo.attach(9);
}

void loop() {
  // Read the values from the microphones
  int servo_pos;
  if (analogRead(mic1_pin) > MIC_THRESHOLD || analogRead(mic2_pin) > MIC_THRESHOLD || analogRead(mic3_pin) > MIC_THRESHOLD )
  {

    // Calculate the average power level for each microphone
    int mic1_avg = 0;
    int mic2_avg = 0;
    int mic3_avg = 0;

    for (int i = 0; i < NUM_SAMPLES; i++) 
    {
      mic1_levels[i] = analogRead(mic1_pin);
      mic2_levels[i] = analogRead(mic2_pin);
      mic3_levels[i] = analogRead(mic3_pin);
    }
 
    int max1 = 0;
    int max2 = 0;
    int max3 = 0;

    for (int i = 0; i < NUM_SAMPLES; i++) {
      mic1_avg += mic1_levels[i];
      mic2_avg += mic2_levels[i];
      mic3_avg += mic3_levels[i];
          
    max1 = max(mic1_levels[i],max1);
    max2 = max(mic2_levels[i],max2);
    max3 = max(mic3_levels[i],max3);

    }

    mic1_avg /= NUM_SAMPLES;
    mic2_avg /= NUM_SAMPLES;
    mic3_avg /= NUM_SAMPLES;



    // Serial.print("\nmic 1:");
    // Serial.print(max1);
    // Serial.print("\nmic 2:");
    // Serial.print(max2);
    // Serial.print("\nmic 3:");   
    // Serial.print(max3);


    // Define the vectors for each microphone in polar form
    //double mic1_vector[] = {120, mic1_avg};
    //double mic2_vector[] = {0, mic2_avg};
   // double mic3_vector[] = {240, mic3_avg};

    // Define the vectors for each microphone in polar form
    double mic1_vector[] = {120, max1};
    double mic2_vector[] = {0, max2};
    double mic3_vector[] = {240, max3};

    // Convert the vectors to rectangular form
    double mic1_rect[] = {mic1_vector[1] * cos(mic1_vector[0] * M_PI / 180), mic1_vector[1] * sin(mic1_vector[0] * M_PI / 180)};
    double mic2_rect[] = {mic2_vector[1] * cos(mic2_vector[0] * M_PI / 180), mic2_vector[1] * sin(mic2_vector[0] * M_PI / 180)};
    double mic3_rect[] = {mic3_vector[1] * cos(mic3_vector[0] * M_PI / 180),  mic3_vector[1] * sin(mic3_vector[0] * M_PI / 180)};

    // Add the vectors
    double result_x = mic1_rect[0] + mic2_rect[0] + mic3_rect[0];
    double result_y = mic1_rect[1] + mic2_rect[1] + mic3_rect[1];


    Serial.print("\nX:");
    Serial.print(result_x);
    Serial.print("\nY:");
    Serial.print(result_y);
    Serial.print("\n");


    // Convert the result back to polar form
    double result_magnitude = sqrt(result_x * result_x + result_y * result_y);
    double result_angle = atan2(result_y, result_x) * 180 / M_PI;
    // Map the angle to a servo position
    //int servo_pos = map(result_angle, -180, 180, 0, 180);
    servo_pos = map(result_angle, -180, 180, 0, 360); 
    // Move the servo to the calculated position
 
    //servo.write(result_angle);
    servo.write(result_angle);
    delay(3000);
  }
 

}


  
