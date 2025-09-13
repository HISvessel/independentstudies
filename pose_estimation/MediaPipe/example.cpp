#include <iostream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

 /*this is a sample code for learning MediaPipe's pipelines*/
string protoG = R"{
input_stream: 'in'
output_stream: 'out'
node {
    calculator: 'PassThroughCalculator'
    input_stream: 'in'
    output_stream: 'out1'
}
node {
    calculator: 'PassThroughCalculator'
    intput_stream: 'in'
    output_stream: 'out1'
}
}";

/*parse config, create a graph*/
mediapipe::CalculatorGraphConfig = 
    mediapipe::ParseTextProtoOrDie<mediapipe::CalculatorGraphConfig>(protoG)

mediapipe::CalculatorGraph graph;
MP_RETURN_IF_ERROR(graph.Initialize(config));

/*adds observer for the output stream*/
auto cb = [](const mediapipe::Packet &packet)->mediapipe::Status{
    cout << packet.Timestamp() << ": RECIEVED" << packet.Get<double>() << endl;
    return mediapipe::OKStatus();
}
MP_RETURN_IF_ERROR(graph.ObservedOutputStream('out', cb));
MP_RETURN_IF_ERROR(graph.StartRun({}));