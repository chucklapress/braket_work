
# step 1 openqasm script:


bell_pair_with_pulse = """

OPENQASM 3.0;
cal {
    waveform q27_q124_cz_wfm = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00021019328936380065, 0.0008644760431374357, 0.003028104466884364, 0.009058671036471382, 0.02322670104785881, 0.05128438687551476, 0.09812230691191462, 0.16403303942241076, 0.24221990600377236, 0.32040677258513395, 0.38631750509563006, 0.43315542513203, 0.4612131109596859, 0.4753811409710734, 0.4814117075406603, 0.48357533596440727, 0.48422961871818093, 0.4843963766398558, 0.4844321964728096, 0.4844386806183817, 0.4844396697373718, 0.48443979687791755, 0.48443981064783953, 0.48443981190433844, 0.4844398120009317, 0.48443981200718716, 0.4844398120075284, 0.48443981200754405, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.4844398120075447, 0.48443981200754405, 0.4844398120075284, 0.48443981200718716, 0.4844398120009317, 0.48443981190433844, 0.48443981064783953, 0.48443979687791755, 0.4844396697373718, 0.4844386806183817, 0.4844321964728096, 0.4843963766398558, 0.48422961871818093, 0.48357533596440727, 0.4814117075406603, 0.4753811409710734, 0.46121311095968553, 0.4331554251320285, 0.38631750509562957, 0.32040677258513167, 0.24221990600377236, 0.16403303942240913, 0.0981223069119151, 0.0512843868755143, 0.023226701047858084, 0.009058671036471328, 0.0030281044668842563, 0.0008644760431374626, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
}
defcal h $27 {
    rz(pi) $27;
    rx(pi/2) $27;
    rz(pi/2) $27;
    rx(-pi/2) $27;
}
defcal h $124 {
    rz(pi) $124;
    rx(pi/2) $124;
    rz(pi/2) $124;
    rx(-pi/2) $124;
}
defcal cz $27, $124 {
    barrier q27_rf_frame, q124_rf_frame, q27_q124_cz_frame;
    play(q27_q124_cz_frame, q27_q124_cz_wfm);
    delay[124ns] q27_rf_frame;
    shift_phase(q27_rf_frame, 1.1733407221086924);
    delay[124ns] q124_rf_frame;
    shift_phase(q124_rf_frame, 6.269846678712192);
    barrier q27_rf_frame, q124_rf_frame, q27_q124_cz_frame;
}
bit[2] c;
h $27;
h $124;
cz $27, $124;
h $124;
c[0] = measure $27;
c[1] = measure $124;
"""


# step 2 establish hardware to run program


from braket.aws import AwsDevice
from braket.ir.openqasm import Program as OpenQASMProgram
aspen_m = AwsDevice("arn:aws:braket:us-west-1::device/qpu/rigetti/Aspen-M-3")


# step 3 call task run and measure results


bell_pair_with_pulses_task = aspen_m.run(OpenQASMProgram(source=bell_pair_with_pulse), shots = 50)
results = bell_pair_with_pulses_task.result()
print("results:", results)


# end of script