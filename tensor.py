import torch

def speaker_embeddings():
    speaker_embeddings = torch.tensor([[-7.4154e-02, -1.5906e-02,  2.2947e-02,  3.9243e-02, -6.1713e-02,
         -3.5635e-02, -9.9613e-03, -3.4536e-03,  6.5565e-05,  2.1907e-02,
         -4.8080e-02, -4.5261e-02,  3.7401e-02,  2.3455e-02, -8.9647e-03,
          6.1811e-02, -2.2997e-02,  7.5770e-03,  1.7576e-02, -6.8785e-03,
          4.6602e-02,  8.3549e-03, -1.9803e-02, -4.6806e-02, -6.7509e-02,
         -6.0809e-03, -2.8296e-02,  6.3677e-02,  4.6826e-02,  1.3593e-02,
         -1.9751e-03,  2.6807e-02, -4.6565e-03, -2.0063e-02,  4.1433e-03,
         -7.0433e-02,  2.0074e-02,  5.3514e-02,  3.3106e-03, -8.1318e-02,
          5.3540e-02,  1.0903e-02,  4.6139e-02,  4.1969e-02,  1.5213e-02,
         -1.3780e-01, -2.0464e-02,  1.4440e-02, -4.3900e-02,  4.6053e-02,
          9.5860e-03,  4.9765e-02,  4.9761e-02,  1.2901e-02, -1.0115e-01,
         -1.0995e-02, -2.0278e-02,  6.0613e-03,  5.4832e-02, -1.1278e-02,
          6.1276e-03, -1.1460e-02, -1.4483e-02,  7.8415e-02, -3.8691e-02,
          3.6960e-02,  1.1383e-03, -6.8034e-02, -7.4391e-02, -4.9159e-02,
          3.2064e-02,  1.2251e-02, -2.3957e-02,  1.3264e-02,  5.6213e-02,
          2.8288e-02,  1.9899e-02,  5.6202e-02, -5.5230e-02, -8.6016e-02,
         -2.9242e-02, -5.5230e-02, -8.0636e-02, -4.5888e-02, -3.3105e-02,
         -4.3178e-02, -7.5166e-02,  8.6420e-02,  3.2853e-02, -1.3616e-02,
          2.7951e-02, -1.1575e-01,  1.1292e-02, -3.9514e-02,  1.2649e-02,
         -3.5977e-02,  1.2981e-02,  5.8359e-02, -2.5467e-02, -8.3012e-02,
         -2.0216e-02, -1.6046e-02, -4.3063e-02,  2.1346e-02,  3.9661e-02,
         -4.9774e-03,  2.4102e-02,  7.1665e-02,  1.5349e-02,  9.0614e-03,
         -7.0513e-02,  2.8949e-02,  6.2169e-02,  1.2027e-02,  2.5990e-02,
          6.9614e-02, -7.4836e-02,  1.2049e-02, -2.0372e-02,  2.1312e-02,
         -5.4053e-03, -5.5167e-02,  1.3297e-02,  7.1627e-02, -6.7178e-02,
          3.8641e-02, -8.1065e-02,  2.1674e-02,  5.4541e-02,  2.5969e-02,
          2.8821e-02,  2.3049e-02,  3.5455e-03,  3.5071e-02,  1.8392e-02,
         -9.8374e-02, -3.7621e-02,  6.6594e-03, -6.9162e-02,  1.0762e-02,
          1.1187e-02,  3.5782e-03,  3.4250e-02, -9.9529e-03, -5.4364e-02,
          2.0030e-02, -2.8972e-02, -2.2669e-03,  4.2164e-02, -8.2306e-02,
          3.6548e-02, -3.7538e-02, -7.6774e-02,  1.7024e-02, -3.9410e-02,
          3.3575e-02,  7.2378e-03, -5.4887e-02, -8.1206e-02,  2.0025e-02,
          4.5636e-02, -5.1637e-03,  2.4121e-02, -2.0635e-02,  3.4499e-02,
          8.4503e-03,  3.5339e-02,  3.8424e-02,  1.9508e-02,  3.8396e-02,
         -5.8030e-02, -6.8892e-02,  6.1081e-02, -4.9394e-02, -2.2318e-02,
          7.4793e-03, -4.2689e-02,  3.7029e-02,  1.4075e-02, -5.8286e-02,
          2.3773e-02, -6.4640e-02, -3.9312e-03,  2.5538e-02, -6.0984e-02,
         -9.6645e-03,  4.1741e-02,  1.2127e-02, -4.3571e-02, -9.0033e-02,
         -2.6753e-02,  1.9946e-02, -7.1794e-02,  2.6281e-02,  4.2655e-02,
         -2.7114e-02,  1.4762e-02, -1.7471e-02,  5.1220e-02,  1.3297e-02,
          3.0171e-02,  1.2996e-02, -8.1938e-02,  7.2992e-03,  1.8458e-02,
          1.6231e-02,  9.1963e-02, -2.2650e-02,  1.1425e-02, -5.3069e-02,
          4.6099e-03, -7.2997e-02, -4.6868e-02,  4.2548e-02, -5.9426e-02,
          2.5587e-03,  8.7465e-02, -6.7129e-02,  4.9709e-02,  5.2144e-02,
         -5.5973e-02,  4.6395e-02, -8.6465e-02, -7.7241e-04, -3.4209e-02,
          5.2857e-02,  3.4389e-02,  6.7562e-02,  2.8617e-02,  4.0374e-02,
         -4.9713e-03,  1.8338e-02,  9.3764e-03, -3.7105e-02,  8.7924e-03,
         -5.6115e-02,  1.3716e-02,  4.3999e-02, -3.0572e-03,  8.8965e-02,
         -5.1681e-02,  2.2660e-02, -8.9623e-02,  5.6373e-03, -7.1666e-02,
          6.4013e-03,  3.7982e-02,  1.4717e-02,  1.1230e-02,  2.5597e-02,
          4.7178e-02,  1.1457e-02,  9.3460e-03, -5.1110e-02,  2.0169e-03,
          1.7157e-02,  2.6152e-02,  1.0549e-03, -1.5423e-02,  4.0246e-02,
          1.1864e-02, -9.0615e-02,  2.1485e-02,  2.9216e-02,  3.5086e-03,
          3.2574e-02,  3.1184e-02,  3.9342e-02,  1.7392e-02, -4.9529e-02,
          1.9505e-02, -1.8653e-02, -1.8245e-02, -2.9087e-02, -6.4355e-02,
          4.9816e-02,  2.6061e-02,  3.2421e-02, -9.7061e-02, -2.4050e-02,
         -1.8466e-02,  5.0169e-02,  1.2805e-02, -6.9982e-02,  2.3800e-02,
          2.9925e-02,  3.3350e-02,  6.4443e-02, -9.2664e-02,  4.6480e-03,
          1.6210e-03,  1.8001e-02, -1.0971e-02, -3.4978e-02, -3.7319e-02,
          4.1185e-02,  1.3505e-02,  1.9150e-02,  5.8681e-02,  5.7560e-03,
         -1.1363e-02,  2.7022e-02,  1.8791e-02, -5.8858e-02,  1.5265e-02,
          3.7924e-02,  3.2706e-02, -4.9417e-03, -4.0816e-03, -5.0133e-03,
          6.6556e-02,  2.8274e-02, -5.8698e-03,  1.1565e-02, -8.3422e-02,
         -7.5798e-02, -3.2658e-02,  5.0126e-03, -5.6561e-02,  5.4205e-02,
         -2.8388e-02,  3.5064e-02, -4.9121e-02,  3.1006e-03,  4.1630e-02,
         -5.9150e-02,  5.6923e-02,  4.6132e-02, -9.9967e-02, -9.2203e-02,
         -7.7813e-02,  1.7408e-02,  1.0046e-02,  3.2996e-02, -6.6164e-02,
          2.3025e-02,  2.3263e-02, -5.8248e-02,  1.3899e-02, -1.2209e-02,
          1.2693e-03, -5.6666e-02,  5.3443e-02,  3.5788e-02, -9.8073e-02,
          9.6703e-03,  1.5079e-03,  2.8788e-02, -3.7118e-02, -8.0610e-02,
         -6.9320e-02, -4.3867e-03, -4.7096e-02,  1.1962e-01,  4.7118e-02,
         -4.3830e-02, -7.1682e-03,  6.4805e-02, -5.9566e-02, -3.2761e-02,
         -7.7035e-02, -9.6765e-03,  2.1148e-02, -5.6175e-03,  3.5023e-02,
         -5.9265e-02, -5.5008e-02,  2.2201e-03,  2.9149e-03,  5.3317e-02,
          1.1396e-02,  5.4093e-02, -9.7267e-02, -1.3389e-02, -1.2035e-02,
         -3.3950e-03,  4.0551e-02,  1.6641e-02,  7.1378e-02,  1.4534e-02,
         -5.7181e-02, -1.0112e-01,  1.2857e-02,  1.3203e-02,  4.3786e-02,
         -4.3937e-03,  1.5593e-02, -4.7267e-02,  5.0260e-02,  4.7092e-02,
          8.3999e-03,  8.4896e-03, -8.3017e-02,  1.9094e-02,  3.9145e-02,
          3.6965e-04,  2.4273e-02, -7.0740e-02,  3.7505e-02,  7.9707e-03,
         -2.5365e-02, -3.4271e-02,  9.6161e-02,  2.2815e-02,  2.5634e-02,
          6.8732e-03,  1.2374e-02, -3.4949e-03, -4.9957e-02, -5.0915e-02,
         -5.6683e-02,  5.0065e-03,  2.0185e-02, -1.8180e-02,  3.8471e-02,
         -7.2645e-02, -1.7927e-02, -9.9017e-02, -1.3515e-01, -9.3793e-02,
         -8.2964e-02,  3.2741e-02,  4.7427e-02, -1.7804e-02, -3.6745e-02,
          1.6186e-02,  5.7527e-02,  5.2268e-02,  2.7272e-02, -5.0203e-02,
         -5.7382e-02, -2.1122e-02, -2.3812e-02,  5.8005e-03,  1.3973e-02,
         -3.5732e-04,  3.1622e-02, -1.4761e-04, -7.7269e-03, -5.8271e-02,
         -3.2955e-02,  2.5373e-02,  2.0877e-02, -3.1536e-04, -5.1553e-02,
          1.7048e-02,  2.1065e-02,  1.3775e-02,  7.1427e-03, -1.1359e-02,
          2.2933e-02,  4.1055e-02,  3.3245e-02,  7.9644e-02, -1.1313e-02,
         -1.8209e-02,  2.5051e-02, -8.2459e-02, -5.9398e-02,  4.3348e-02,
         -1.3458e-02,  1.2181e-02,  5.3466e-02, -1.8879e-03, -4.4908e-02,
          4.0940e-02,  2.7616e-02, -3.9160e-02,  4.3746e-02, -7.8092e-05,
         -4.3155e-03,  4.3624e-02,  3.2331e-02,  5.5303e-03, -5.1708e-02,
         -7.3163e-02, -2.6620e-04, -4.6545e-03,  4.8307e-02,  4.4577e-02,
         -4.0848e-02, -5.7069e-02,  1.6721e-02,  9.0564e-03,  3.9430e-02,
          7.5166e-02, -6.0188e-02, -3.4520e-03, -1.4739e-02, -1.4246e-02,
         -8.7310e-02,  1.5523e-03, -5.3883e-02,  2.4998e-02, -4.9384e-02,
          4.7550e-02, -6.2472e-02,  1.9427e-02, -5.0676e-02, -6.2309e-02,
          9.6085e-03,  3.4866e-02, -4.9666e-02,  1.6355e-02,  2.0948e-02,
         -1.0997e-02, -1.1647e-02,  3.6383e-02,  6.6882e-02,  2.4936e-02,
          4.9996e-02, -4.9682e-02
    ]])
    return speaker_embeddings
    
def speaker_embeddings2():
    speaker_embeddings2 = torch.tensor([[-0.0753, -0.0036,  0.0468,  0.0310,  0.0200, -0.0186, -0.0710, -0.0408,
          0.0416,  0.0219, -0.0866, -0.0845,  0.0668,  0.0108,  0.0119,  0.0637,
         -0.0124,  0.0298,  0.0158,  0.0183,  0.0413,  0.0224, -0.0191, -0.0363,
         -0.0732, -0.0049, -0.0563,  0.0170,  0.0345,  0.0500, -0.0022,  0.0256,
          0.0139,  0.0113,  0.0174, -0.0632,  0.0377,  0.0846, -0.0459, -0.0520,
          0.0218, -0.0313,  0.0347,  0.0257,  0.0167, -0.1371, -0.0208,  0.0126,
         -0.0782,  0.0497,  0.0096,  0.0154,  0.0145,  0.0179, -0.1048, -0.0126,
          0.0391,  0.0129,  0.0120,  0.0392,  0.0203, -0.0104, -0.0159,  0.0126,
         -0.0014,  0.0329,  0.0247, -0.0235, -0.0653, -0.0555,  0.0365,  0.0122,
         -0.0310,  0.0166,  0.0206,  0.0378,  0.0275,  0.0377, -0.0588, -0.0636,
         -0.0544, -0.0505, -0.0616, -0.0713, -0.0327, -0.0535, -0.0770,  0.0504,
          0.0335,  0.0396,  0.0290, -0.0728,  0.0208, -0.0670,  0.0418, -0.0606,
          0.0398,  0.0360, -0.0349, -0.0984,  0.0236, -0.0527, -0.0728,  0.0235,
          0.0694, -0.0330,  0.0384,  0.0429,  0.0265,  0.0082, -0.0621, -0.0080,
          0.0763, -0.0010,  0.0442,  0.0665, -0.0762, -0.0298, -0.0790, -0.0156,
          0.0204, -0.0806,  0.0432,  0.0232, -0.0616,  0.0595, -0.0850,  0.0207,
          0.0219,  0.0126, -0.0228,  0.0388,  0.0191,  0.0649,  0.0164, -0.0576,
         -0.0512,  0.0222, -0.0716, -0.0286,  0.0229,  0.0027, -0.0046,  0.0451,
         -0.0800,  0.0332, -0.0230, -0.0301,  0.0565, -0.0976,  0.0202, -0.0641,
         -0.0448,  0.0439,  0.0293,  0.0263,  0.0447, -0.0827, -0.0529,  0.0307,
          0.0268, -0.0027,  0.0226, -0.0614, -0.0012,  0.0076,  0.0313,  0.0201,
          0.0278,  0.0228, -0.0579, -0.0409,  0.0376, -0.0630, -0.0496,  0.0203,
         -0.0394,  0.0058,  0.0444, -0.0586,  0.0172, -0.0620,  0.0192, -0.0054,
         -0.0533, -0.0088,  0.0331,  0.0411, -0.0396, -0.0582, -0.0058,  0.0435,
         -0.0550,  0.0067,  0.0516,  0.0238,  0.0323, -0.0056,  0.0468,  0.0004,
          0.0127,  0.0239, -0.0567,  0.0042,  0.0239,  0.0238,  0.0317, -0.0006,
          0.0255, -0.0346,  0.0030, -0.0484, -0.0572,  0.0565, -0.0515,  0.0581,
          0.0212, -0.0445,  0.0488,  0.0790, -0.0521,  0.0319, -0.0752, -0.0315,
          0.0298,  0.0407,  0.0783,  0.0922,  0.0253,  0.0498, -0.0231,  0.0308,
          0.0290, -0.0223,  0.0222, -0.0157,  0.0268,  0.0145, -0.0014,  0.0678,
         -0.0456,  0.0259, -0.0726,  0.0209, -0.0404,  0.0230,  0.0578,  0.0371,
          0.0424,  0.0532,  0.0300,  0.0073,  0.0099, -0.0488,  0.0124,  0.0261,
          0.0289,  0.0473, -0.0710,  0.0557,  0.0117, -0.0668,  0.0285,  0.0483,
          0.0031,  0.0151,  0.0159,  0.0147,  0.0414, -0.0407,  0.0632, -0.0211,
          0.0022, -0.0285, -0.0845,  0.0380,  0.0148,  0.0530, -0.0774, -0.0377,
          0.0072,  0.0435,  0.0212, -0.0946, -0.0285,  0.0350,  0.0159,  0.0555,
         -0.0990,  0.0059,  0.0185,  0.0130, -0.0247, -0.0079, -0.0046, -0.0020,
          0.0194,  0.0212,  0.0667,  0.0245,  0.0242,  0.0182,  0.0180, -0.0576,
          0.0147,  0.0843,  0.0296,  0.0175,  0.0514, -0.0053,  0.0364,  0.0573,
          0.0024,  0.0224, -0.0906, -0.0437, -0.0299,  0.0104, -0.0649,  0.0518,
         -0.0322,  0.0368, -0.0254,  0.0015,  0.0306, -0.0352,  0.0689,  0.0649,
         -0.0690, -0.0878, -0.0486,  0.0147,  0.0168,  0.0391, -0.0673,  0.0083,
          0.0487,  0.0109,  0.0005, -0.0503,  0.0426, -0.0654, -0.0009,  0.0272,
         -0.0580,  0.0369,  0.0094,  0.0167, -0.0397, -0.0847, -0.0619, -0.0217,
         -0.0521,  0.1169,  0.0183, -0.0468, -0.0073,  0.0577, -0.0456,  0.0224,
         -0.0877,  0.0136,  0.0140, -0.0012,  0.0453,  0.0136, -0.0612,  0.0130,
          0.0102,  0.0405,  0.0126,  0.0402, -0.0803,  0.0280, -0.0136, -0.0026,
          0.0389,  0.0258,  0.0543,  0.0294, -0.0780, -0.1013,  0.0069,  0.0335,
          0.0139, -0.0473,  0.0650, -0.0599,  0.0451,  0.0620,  0.0337,  0.0343,
         -0.0444,  0.0214,  0.0284, -0.0046,  0.0537, -0.0665,  0.0702, -0.0109,
         -0.0065, -0.0607,  0.0155, -0.0286,  0.0129,  0.0102,  0.0167, -0.0855,
         -0.0252, -0.0898, -0.0306,  0.0347,  0.0246, -0.0169,  0.0594, -0.0639,
         -0.0231, -0.0803, -0.1447, -0.0396, -0.0632,  0.0115,  0.0239, -0.0405,
         -0.0386,  0.0399,  0.0610,  0.0035,  0.0369, -0.0535, -0.0421, -0.0167,
         -0.0199,  0.0021,  0.0320,  0.0241,  0.0572,  0.0092, -0.0480, -0.0828,
         -0.0042,  0.0279,  0.0214, -0.0008,  0.0224,  0.0335,  0.0159,  0.0101,
          0.0156, -0.0129,  0.0263,  0.0106,  0.0416,  0.0311,  0.0141,  0.0153,
          0.0079, -0.0905, -0.0561,  0.0425, -0.0140, -0.0030,  0.0409,  0.0463,
         -0.0695,  0.0632,  0.0344, -0.0457,  0.0225,  0.0383, -0.0034,  0.0426,
          0.0260,  0.0049, -0.0597, -0.0738, -0.0016, -0.0052,  0.0422,  0.0259,
         -0.0562, -0.0623,  0.0085,  0.0295,  0.0085,  0.0646, -0.0581,  0.0165,
         -0.0256, -0.0116, -0.0536,  0.0311, -0.0605,  0.0097,  0.0031,  0.0416,
         -0.0366, -0.0117, -0.0845, -0.0581,  0.0097,  0.0348, -0.0623,  0.0332,
          0.0153, -0.0111, -0.0406,  0.0428,  0.0607, -0.0208,  0.0359, -0.0551
    ]])
    return speaker_embeddings2