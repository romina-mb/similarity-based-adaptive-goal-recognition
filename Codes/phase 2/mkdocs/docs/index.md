# Experiments and Results

### Detailed Results


This table shows the detailed results for each adaptive GR system, performing in different problem instances under three types of environmental drift. The selected problem instances all have significant environmental changes.

`drift`: the type of environmental changes <br />
`domain`: the domain of the agent acting in <br />
`system`: a GR system (adaptive or conventional) <br />
`problem`: a specific problem instance in a domain <br />
`1 - 50`: the average accuracy for a GR system performing from timestep 1 to timestep 50 <br />
`51 - 100`: the average accuracy for a GR system performing from timestep 51 to timestep 100 <br />
`101 - 150`: the average accuracy for a GR system performing from timestep 101 to timestep 150 <br />
`151 - 200`: the average accuracy for a GR system performing from timestep 151 to timestep 200

The environment changes after every 50 timesteps, either suddenly or gradually. If there are no GR tasks during a particular period, the value `nan` is used.

|  drift |  domain  |    system     |  problem  |   1 - 50   |   51 - 100   |   101 - 150   |   151 - 200   |
|:-------|:---------|:--------------|:----------|:-----------|:-------------|:--------------|:--------------|
| reoccurring | satellite |no relearn         | p01  | 0.699  | 0.494  | 0.670 | 0.505 |
| reoccurring | satellite |open loop          | p01  | 0.848  | 0.759  | 0.830 | 0.741 |
| reoccurring | satellite |closed loop ave    | p01  | 0.773  | 0.693  | 0.743 | 0.686 |
| reoccurring | satellite |closed loop trend  | p01  | 0.723  | 0.494  | 0.627 | 0.489 |
| reoccurring | blocks-world |no relearn         | p01  | 0.660  | 0.498  | 0.658 | 0.500 |
| reoccurring | blocks-world |open loop          | p01  | 0.523  | 0.503  | 0.535 | 0.528 |
| reoccurring | blocks-world |closed loop ave    | p01  | 0.939  | 0.819  | 0.936 | 0.804 |
| reoccurring | blocks-world |closed loop trend  | p01  | 0.933  | 0.755  | 0.923 | 0.786 |
| reoccurring | zeno-travel |no relearn         | p06  | 0.943  | 0.538  | 0.960 | 0.531 |
| reoccurring | zeno-travel |open loop          | p06  | 0.699  | 0.676  | 0.720 | 0.683 |
| reoccurring | zeno-travel |closed loop ave    | p06  | 0.761  | 0.770  | 0.732 | 0.761 |
| reoccurring | zeno-travel |closed loop trend  | p06  | 0.809  | 0.723  | 0.775 | 0.680 |
| reoccurring | satellite |no relearn         | p06  | 0.911  | 0.500  | 0.913 | 0.500 |
| reoccurring | satellite |open loop          | p06  | 0.918  | 0.829  | 0.907 | 0.837 |
| reoccurring | satellite |closed loop ave    | p06  | 0.871  | 0.706  | 0.848 | 0.698 |
| reoccurring | satellite |closed loop trend  | p06  | 0.756  | 0.666  | 0.751 | 0.706 |
| reoccurring | logistics |no relearn         | p07  | 0.961  | 0.781  | 0.956 | 0.786 |
| reoccurring | logistics |open loop          | p07  | 0.902  | 0.700  | 0.892 | 0.708 |
| reoccurring | logistics |closed loop ave    | p07  | 0.785  | 0.676  | 0.776 | 0.657 |
| reoccurring | logistics |closed loop trend  | p07  | 0.829  | 0.781  | 0.861 | 0.758 |
| reoccurring | satellite |no relearn         | p04  | 0.962  | 0.502  | 0.950 | 0.506 |
| reoccurring | satellite |open loop          | p04  | 0.833  | 0.690  | 0.833 | 0.690 |
| reoccurring | satellite |closed loop ave    | p04  | 0.997  | 0.797  | 0.997 | 0.779 |
| reoccurring | satellite |closed loop trend  | p04  | 0.853  | 0.563  | 0.846 | 0.573 |
| reoccurring | rovers |no relearn         | p03  | 0.917  | 0.812  | 0.899 | 0.778 |
| reoccurring | rovers |open loop          | p03  | 0.989  | 0.683  | 0.983 | 0.683 |
| reoccurring | rovers |closed loop ave    | p03  | 0.994  | 0.633  | 0.993 | 0.633 |
| reoccurring | rovers |closed loop trend  | p03  | 0.749  | 0.480  | 0.746 | 0.485 |
| reoccurring | driverlog |no relearn         | p02  | 0.809  | 0.547  | 0.788 | 0.555 |
| reoccurring | driverlog |open loop          | p02  | 0.999  | 0.882  | 0.999 | 0.881 |
| reoccurring | driverlog |closed loop ave    | p02  | 0.796  | 0.710  | 0.810 | 0.717 |
| reoccurring | driverlog |closed loop trend  | p02  | 0.537  | 0.501  | 0.545 | 0.498 |
| reoccurring | easy-ipc-grid |no relearn         | p5-10-10  | 0.737  | 0.568  | 0.761 | 0.582 |
| reoccurring | easy-ipc-grid |open loop          | p5-10-10  | 0.748  | 0.673  | 0.709 | 0.698 |
| reoccurring | easy-ipc-grid |closed loop ave    | p5-10-10  | 0.678  | 0.604  | 0.674 | 0.616 |
| reoccurring | easy-ipc-grid |closed loop trend  | p5-10-10  | 0.746  | 0.615  | 0.741 | 0.634 |
| reoccurring | logistics |no relearn         | p06  | 0.969  | 0.861  | 0.968 | 0.858 |
| reoccurring | logistics |open loop          | p06  | 0.604  | 0.496  | 0.596 | 0.503 |
| reoccurring | logistics |closed loop ave    | p06  | 0.751  | 0.693  | 0.771 | 0.679 |
| reoccurring | logistics |closed loop trend  | p06  | 0.828  | 0.698  | 0.845 | 0.712 |
| reoccurring | rovers |no relearn         | p07  | 1.000  | 0.767  | 1.000 | 0.767 |
| reoccurring | rovers |open loop          | p07  | 0.597  | 0.836  | 0.593 | 0.848 |
| reoccurring | rovers |closed loop ave    | p07  | 0.991  | 0.730  | 0.991 | 0.729 |
| reoccurring | rovers |closed loop trend  | p07  | 0.900  | 0.633  | 0.900 | 0.633 |
| reoccurring | logistics |no relearn         | p03  | 0.894  | 0.608  | 0.901 | 0.622 |
| reoccurring | logistics |open loop          | p03  | 1.000  | 0.790  | 1.000 | 0.789 |
| reoccurring | logistics |closed loop ave    | p03  | 0.743  | 0.810  | 0.724 | 0.804 |
| reoccurring | logistics |closed loop trend  | p03  | 0.578  | 0.597  | 0.606 | 0.586 |
| reoccurring | satellite |no relearn         | p07  | 0.916  | 0.500  | 0.924 | 0.500 |
| reoccurring | satellite |open loop          | p07  | 0.841  | 0.571  | 0.844 | 0.566 |
| reoccurring | satellite |closed loop ave    | p07  | 0.686  | 0.633  | 0.690 | 0.654 |
| reoccurring | satellite |closed loop trend  | p07  | 0.727  | 0.602  | 0.718 | 0.625 |
| reoccurring | miconic |no relearn         | p07  | 1.000  | 0.767  | 1.000 | 0.767 |
| reoccurring | miconic |open loop          | p07  | 0.823  | 0.722  | 0.827 | 0.754 |
| reoccurring | miconic |closed loop ave    | p07  | 0.949  | 0.821  | 0.945 | 0.816 |
| reoccurring | miconic |closed loop trend  | p07  | 0.772  | 0.674  | 0.762 | 0.691 |
| reoccurring | rovers |no relearn         | p07  | 1.000  | 0.876  | 0.930 | 0.876 |
| reoccurring | rovers |open loop          | p07  | 0.597  | 0.836  | 0.598 | 0.839 |
| reoccurring | rovers |closed loop ave    | p07  | 0.911  | 0.500  | 0.838 | 0.500 |
| reoccurring | rovers |closed loop trend  | p07  | 0.881  | 0.797  | 0.851 | 0.779 |
| reoccurring | satellite |no relearn         | p02  | 0.749  | 0.490  | 0.640 | 0.496 |
| reoccurring | satellite |open loop          | p02  | 0.780  | 0.890  | 0.732 | 0.881 |
| reoccurring | satellite |closed loop ave    | p02  | 1.000  | 0.962  | 0.920 | 0.961 |
| reoccurring | satellite |closed loop trend  | p02  | 0.961  | 0.813  | 0.897 | 0.793 |
| reoccurring | blocks-world |no relearn         | p01  | 0.660  | 0.495  | 0.644 | 0.496 |
| reoccurring | blocks-world |open loop          | p01  | 0.727  | 0.640  | 0.717 | 0.633 |
| reoccurring | blocks-world |closed loop ave    | p01  | 0.846  | 0.783  | 0.850 | 0.777 |
| reoccurring | blocks-world |closed loop trend  | p01  | 0.991  | 0.808  | 0.946 | 0.811 |
| reoccurring | logistics |no relearn         | p02  | 0.887  | 0.782  | 0.807 | 0.822 |
| reoccurring | logistics |open loop          | p02  | 0.686  | 0.633  | 0.690 | 0.654 |
| reoccurring | logistics |closed loop ave    | p02  | 0.748  | 0.673  | 0.709 | 0.698 |
| reoccurring | logistics |closed loop trend  | p02  | 0.997  | 0.885  | 0.888 | 0.970 |
| reoccurring | rovers |no relearn         | p02  | 0.933  | 0.840  | 0.821 | 0.822 |
| reoccurring | rovers |open loop          | p02  | 0.737  | 0.638  | 0.700 | 0.650 |
| reoccurring | rovers |closed loop ave    | p02  | 0.761  | 0.770  | 0.732 | 0.761 |
| reoccurring | rovers |closed loop trend  | p02  | 0.741  | 0.651  | 0.694 | 0.659 |
| reoccurring | dwr |no relearn         | p03  | 0.833  | 0.690  | 0.833 | 0.690 |
| reoccurring | dwr |open loop          | p03  | 0.841  | 0.863  | 0.755 | 0.850 |
| reoccurring | dwr |closed loop ave    | p03  | 0.589  | 0.498  | 0.498 | 0.493 |
| reoccurring | dwr |closed loop trend  | p03  | 0.604  | 0.500  | 0.559 | 0.496 |
| reoccurring | logistics |no relearn         | p03  | 0.949  | 0.821  | 0.945 | 0.816 |
| reoccurring | logistics |open loop          | p03  | 1.000  | 0.957  | 0.945 | 0.957 |
| reoccurring | logistics |closed loop ave    | p03  | 0.994  | 0.933  | 0.950 | 0.920 |
| reoccurring | logistics |closed loop trend  | p03  | 0.918  | 0.819  | 0.915 | 0.832 |
| reoccurring | zeno-travel |no relearn         | p01  | 0.940  | 0.796  | 0.866 | 0.812 |
| reoccurring | zeno-travel |open loop          | p01  | 0.828  | 0.751  | 0.812 | 0.753 |
| reoccurring | zeno-travel |closed loop ave    | p01  | 0.689  | 0.843  | 0.704 | 0.844 |
| reoccurring | zeno-travel |closed loop trend  | p01  | 0.969  | 0.861  | 0.968 | 0.858 |
| reoccurring | satellite |no relearn         | p04  | 0.962  | 0.511  | 0.841 | 0.503 |
| reoccurring | satellite |open loop          | p04  | 0.619  | 0.501  | 0.561 | 0.500 |
| reoccurring | satellite |closed loop ave    | p04  | 0.537  | 0.501  | 0.545 | 0.498 |
| reoccurring | satellite |closed loop trend  | p04  | 0.889  | 0.832  | 0.883 | 0.830 |
| reoccurring | blocks-world |no relearn         | p02  | 0.619  | 0.498  | 0.561 | 0.500 |
| reoccurring | blocks-world |open loop          | p02  | 0.630  | 0.718  | 0.628 | 0.719 |
| reoccurring | blocks-world |closed loop ave    | p02  | 0.608  | 0.847  | 0.584 | 0.832 |
| reoccurring | blocks-world |closed loop trend  | p02  | 1.000  | 0.470  | 0.913 | 0.499 |
| reoccurring | logistics |no relearn         | p03  | 0.949  | 0.821  | 0.945 | 0.865 |
| reoccurring | logistics |open loop          | p03  | 1.000  | 0.876  | 0.930 | 0.876 |
| reoccurring | logistics |closed loop ave    | p03  | 0.638  | 0.641  | 0.612 | 0.650 |
| reoccurring | logistics |closed loop trend  | p03  | 0.878  | 0.796  | 0.851 | 0.779 |
| reoccurring | easy-ipc-grid |no relearn         | p5-5-5  | 0.741  | 0.651  | 0.639 | 0.636 |
| reoccurring | easy-ipc-grid |open loop          | p5-5-5  | 0.614  | 0.781  | 0.586 | 0.812 |
| reoccurring | easy-ipc-grid |closed loop ave    | p5-5-5  | 0.780  | 0.890  | 0.732 | 0.881 |
| reoccurring | easy-ipc-grid |closed loop trend  | p5-5-5  | 0.900  | 0.837  | 0.817 | 0.837 |
| reoccurring | intrusion-detection |no relearn         | p20  | 0.993  | 0.848  | 0.927 | 0.823 |
| reoccurring | intrusion-detection |open loop          | p20  | 0.917  | 0.812  | 0.899 | 0.817 |
| reoccurring | intrusion-detection |closed loop ave    | p20  | 0.537  | 0.501  | 0.545 | 0.498 |
| reoccurring | intrusion-detection |closed loop trend  | p20  | 0.933  | 0.840  | 0.793 | 0.804 |
| reoccurring | logistics |no relearn         | p05  | 0.939  | 0.848  | 0.834 | 0.900 |
| reoccurring | logistics |open loop          | p05  | 0.914  | 0.833  | 0.853 | 0.838 |
| reoccurring | logistics |closed loop ave    | p05  | 0.785  | 0.714  | 0.731 | 0.715 |
| reoccurring | logistics |closed loop trend  | p05  | 0.796  | 0.734  | 0.790 | 0.755 |
| reoccurring | logistics |no relearn         | p06  | 0.969  | 0.861  | 0.968 | 0.858 |
| reoccurring | logistics |open loop          | p06  | 1.000  | 0.957  | 0.945 | 0.957 |
| reoccurring | logistics |closed loop ave    | p06  | 0.740  | 0.658  | 0.729 | 0.638 |
| reoccurring | logistics |closed loop trend  | p06  | 0.999  | 0.920  | 0.965 | 0.949 |
| reoccurring | satellite |no relearn         | p06  | 0.911  | 0.500  | 0.838 | 0.500 |
| reoccurring | satellite |open loop          | p06  | 0.650  | 0.493  | 0.645 | 0.502 |
| reoccurring | satellite |closed loop ave    | p06  | 0.873  | 0.759  | 0.868 | 0.824 |
| reoccurring | satellite |closed loop trend  | p06  | 0.646  | 0.499  | 0.565 | 0.506 |
| gradual | satellite |no relearn         | p01  | 0.724  | 0.618  | 0.480 | nan |
| gradual | satellite |open loop          | p01  | 0.848  | 0.805  | 0.764 | nan |
| gradual | satellite |closed loop ave    | p01  | 0.761  | 0.730  | 0.649 | nan |
| gradual | satellite |closed loop trend  | p01  | 0.722  | 0.537  | 0.497 | nan |
| gradual | logistics |no relearn         | p01  | 0.916  | 0.781  | 0.915 | nan |
| gradual | logistics |open loop          | p01  | 0.912  | 0.818  | 0.811 | nan |
| gradual | logistics |closed loop ave    | p01  | 0.678  | 0.576  | 0.503 | nan |
| gradual | logistics |closed loop trend  | p01  | 1.000  | 0.943  | 1.000 | nan |
| gradual | blocks-world |no relearn         | p01  | 0.659  | 0.581  | 0.506 | nan |
| gradual | blocks-world |open loop          | p01  | 0.539  | 0.534  | 0.486 | nan |
| gradual | blocks-world |closed loop ave    | p01  | 0.931  | 0.870  | 0.821 | nan |
| gradual | blocks-world |closed loop trend  | p01  | 0.932  | 0.846  | 0.769 | nan |
| gradual | zeno-travel |no relearn         | p06  | 0.944  | 0.719  | 0.543 | nan |
| gradual | zeno-travel |open loop          | p06  | 0.696  | 0.691  | 0.676 | nan |
| gradual | zeno-travel |closed loop ave    | p06  | 0.748  | 0.755  | 0.780 | nan |
| gradual | zeno-travel |closed loop trend  | p06  | 0.766  | 0.782  | 0.725 | nan |
| gradual | satellite |no relearn         | p06  | 0.915  | 0.653  | 0.500 | nan |
| gradual | satellite |open loop          | p06  | 0.912  | 0.880  | 0.847 | nan |
| gradual | satellite |closed loop ave    | p06  | 0.890  | 0.799  | 0.688 | nan |
| gradual | satellite |closed loop trend  | p06  | 0.767  | 0.709  | 0.692 | nan |
| gradual | blocks-world |no relearn         | p05  | 0.598  | 0.541  | 0.494 | nan |
| gradual | blocks-world |open loop          | p05  | 0.627  | 0.690  | 0.756 | nan |
| gradual | blocks-world |closed loop ave    | p05  | 0.759  | 0.651  | 0.597 | nan |
| gradual | blocks-world |closed loop trend  | p05  | 0.721  | 0.696  | 0.703 | nan |
| gradual | logistics |no relearn         | p07  | 0.953  | 0.856  | 0.788 | nan |
| gradual | logistics |open loop          | p07  | 0.893  | 0.808  | 0.708 | nan |
| gradual | logistics |closed loop ave    | p07  | 0.790  | 0.743  | 0.662 | nan |
| gradual | logistics |closed loop trend  | p07  | 0.842  | 0.796  | 0.764 | nan |
| gradual | satellite |no relearn         | p04  | 0.945  | 0.737  | 0.503 | nan |
| gradual | satellite |open loop          | p04  | 0.833  | 0.769  | 0.690 | nan |
| gradual | satellite |closed loop ave    | p04  | 0.997  | 0.881  | 0.764 | nan |
| gradual | satellite |closed loop trend  | p04  | 0.868  | 0.693  | 0.552 | nan |
| gradual | driverlog |no relearn         | p02  | 0.779  | 0.666  | 0.551 | nan |
| gradual | driverlog |open loop          | p02  | 0.999  | 0.934  | 0.889 | nan |
| gradual | driverlog |closed loop ave    | p02  | 0.827  | 0.765  | 0.700 | nan |
| gradual | driverlog |closed loop trend  | p02  | 0.539  | 0.517  | 0.500 | nan |
| gradual | easy-ipc-grid |no relearn         | p5-10-10  | 0.738  | 0.645  | 0.570 | nan |
| gradual | easy-ipc-grid |open loop          | p5-10-10  | 0.733  | 0.713  | 0.676 | nan |
| gradual | easy-ipc-grid |closed loop ave    | p5-10-10  | 0.660  | 0.649  | 0.621 | nan |
| gradual | easy-ipc-grid |closed loop trend  | p5-10-10  | 0.735  | 0.669  | 0.615 | nan |
| gradual | rovers |no relearn         | p07  | 1.000  | 0.881  | 0.767 | nan |
| gradual | rovers |open loop          | p07  | 0.604  | 0.711  | 0.843 | nan |
| gradual | rovers |closed loop ave    | p07  | 0.994  | 0.879  | 0.737 | nan |
| gradual | rovers |closed loop trend  | p07  | 0.900  | 0.759  | 0.633 | nan |
| gradual | logistics |no relearn         | p03  | 0.910  | 0.793  | 0.622 | nan |
| gradual | logistics |open loop          | p03  | 1.000  | 0.870  | 0.788 | nan |
| gradual | logistics |closed loop ave    | p03  | 0.721  | 0.754  | 0.800 | nan |
| gradual | logistics |closed loop trend  | p03  | 0.609  | 0.617  | 0.600 | nan |
| gradual | satellite |no relearn         | p07  | 0.900  | 0.676  | 0.500 | nan |
| gradual | satellite |open loop          | p07  | 0.846  | 0.710  | 0.575 | nan |
| gradual | satellite |closed loop ave    | p07  | 0.709  | 0.660  | 0.640 | nan |
| gradual | satellite |closed loop trend  | p07  | 0.683  | 0.693  | 0.610 | nan |
| gradual | miconic |no relearn         | p07  | 1.000  | 0.862  | 0.767 | nan |
| gradual | miconic |open loop          | p07  | 0.824  | 0.781  | 0.716 | nan |
| gradual | miconic |closed loop ave    | p07  | 0.944  | 0.864  | 0.808 | nan |
| gradual | miconic |closed loop trend  | p07  | 0.785  | 0.756  | 0.667 | nan |
| gradual | satellite |no relearn         | p02  | 0.745  | 0.578  | 0.497 | nan |
| gradual | satellite |open loop          | p02  | 0.780  | 0.787  | 1.000 | nan |
| gradual | satellite |closed loop ave    | p02  | 1.000  | 0.900  | 1.000 | nan |
| gradual | satellite |closed loop trend  | p02  | 0.953  | 0.856  | 0.788 | nan |
| gradual | blocks-world |no relearn         | p01  | 0.659  | 0.581  | 0.504 | nan |
| gradual | blocks-world |open loop          | p01  | 0.683  | 0.693  | 0.620 | nan |
| gradual | blocks-world |closed loop ave    | p01  | 0.846  | 0.806  | 0.750 | nan |
| gradual | blocks-world |closed loop trend  | p01  | 0.994  | 0.879  | 0.834 | nan |
| gradual | logistics |no relearn         | p02  | 0.876  | 0.795  | 0.757 | nan |
| gradual | logistics |open loop          | p02  | 0.709  | 0.679  | 0.721 | nan |
| gradual | logistics |closed loop ave    | p02  | 0.733  | 0.713  | 0.676 | nan |
| gradual | logistics |closed loop trend  | p02  | 0.997  | 0.881  | 0.856 | nan |
| gradual | rovers |no relearn         | p02  | 0.932  | 0.846  | 0.802 | nan |
| gradual | rovers |open loop          | p02  | 0.738  | 0.687  | 0.663 | nan |
| gradual | rovers |closed loop ave    | p02  | 0.748  | 0.755  | 0.780 | nan |
| gradual | rovers |closed loop trend  | p02  | 0.759  | 0.684  | 0.660 | nan |
| gradual | dwr |no relearn         | p01  | 0.868  | 0.753  | 0.833 | nan |
| gradual | dwr |open loop          | p01  | 0.901  | 0.862  | 0.805 | nan |
| gradual | dwr |closed loop ave    | p01  | 0.767  | 0.709  | 0.692 | nan |
| gradual | dwr |closed loop trend  | p01  | 0.539  | 0.534  | 0.476 | nan |
| gradual | dwr |no relearn         | p03  | 0.833  | 0.769  | 0.690 | nan |
| gradual | dwr |open loop          | p03  | 0.846  | 0.777  | 0.924 | nan |
| gradual | dwr |closed loop ave    | p03  | 0.598  | 0.541  | 0.487 | nan |
| gradual | dwr |closed loop trend  | p03  | 0.613  | 0.556  | 0.499 | nan |
| gradual | logistics |no relearn         | p03  | 0.944  | 0.864  | 0.808 | nan |
| gradual | logistics |open loop          | p03  | 1.000  | 0.862  | 1.000 | nan |
| gradual | logistics |closed loop ave    | p03  | 0.994  | 0.847  | 0.983 | nan |
| gradual | logistics |closed loop trend  | p03  | 0.915  | 0.879  | 0.821 | nan |
| gradual | zeno-travel |no relearn         | p01  | 0.940  | 0.851  | 0.832 | nan |
| gradual | zeno-travel |open loop          | p01  | 0.843  | 0.780  | 0.779 | nan |
| gradual | zeno-travel |closed loop ave    | p01  | 0.713  | 0.784  | 0.831 | nan |
| gradual | zeno-travel |closed loop trend  | p01  | 0.967  | 0.911  | 0.867 | nan |
| gradual | satellite |no relearn         | p04  | 0.945  | 0.737  | 0.486 | nan |
| gradual | satellite |open loop          | p04  | 0.615  | 0.552  | 0.505 | nan |
| gradual | satellite |closed loop ave    | p04  | 0.539  | 0.517  | 0.500 | nan |
| gradual | satellite |closed loop trend  | p04  | 0.901  | 0.863  | 0.833 | nan |
| gradual | blocks-world |no relearn         | p02  | 0.615  | 0.557  | 0.503 | nan |
| gradual | blocks-world |open loop          | p02  | 0.619  | 0.632  | 0.692 | nan |
| gradual | blocks-world |closed loop ave    | p02  | 0.602  | 0.724  | 0.860 | nan |
| gradual | blocks-world |closed loop trend  | p02  | 1.000  | 0.763  | 0.497 | nan |
| gradual | easy-ipc-grid |no relearn         | p5-5-5  | 0.759  | 0.661  | 0.640 | nan |
| gradual | easy-ipc-grid |open loop          | p5-5-5  | 0.612  | 0.706  | 0.799 | nan |
| gradual | easy-ipc-grid |closed loop ave    | p5-5-5  | 0.780  | 0.883  | 1.000 | nan |
| gradual | easy-ipc-grid |closed loop trend  | p5-5-5  | 0.900  | 0.935  | 1.000 | nan |
| gradual | intrusion-detection |no relearn         | p20  | 0.993  | 0.902  | 0.867 | nan |
| gradual | intrusion-detection |open loop          | p20  | 0.902  | 0.841  | 0.867 | nan |
| gradual | intrusion-detection |closed loop ave    | p20  | 0.539  | 0.517  | 0.500 | nan |
| gradual | intrusion-detection |closed loop trend  | p20  | 0.932  | 0.846  | 0.808 | nan |
| gradual | dwr |no relearn         | p01  | 0.868  | 0.770  | 0.757 | nan |
| gradual | dwr |open loop          | p01  | 0.779  | 0.755  | 0.776 | nan |
| gradual | dwr |closed loop ave    | p01  | 0.829  | 0.802  | 0.794 | nan |
| gradual | dwr |closed loop trend  | p01  | 0.790  | 0.809  | 0.891 | nan |
| gradual | logistics |no relearn         | p05  | 0.931  | 0.870  | 0.821 | nan |
| gradual | logistics |open loop          | p05  | 0.910  | 0.839  | 0.881 | nan |
| gradual | logistics |closed loop ave    | p05  | 0.708  | 0.743  | 0.759 | nan |
| gradual | logistics |closed loop trend  | p05  | 0.829  | 0.796  | 0.759 | nan |
| gradual | satellite |no relearn         | p06  | 0.915  | 0.653  | 0.500 | nan |
| gradual | satellite |open loop          | p06  | 0.707  | 0.597  | 0.482 | nan |
| gradual | satellite |closed loop ave    | p06  | 0.842  | 0.839  | 0.800 | nan |
| gradual | satellite |closed loop trend  | p06  | 0.637  | 0.561  | 0.499 | nan |
| sudden | satellite |no relearn         | p01  | 0.712  | 0.496  | nan | nan |
| sudden | satellite |open loop          | p01  | 0.821  | 0.738  | nan | nan |
| sudden | satellite |closed loop ave    | p01  | 0.785  | 0.732  | nan | nan |
| sudden | satellite |closed loop trend  | p01  | 0.679  | 0.482  | nan | nan |
| sudden | driverlog |no relearn         | p01  | 0.883  | 0.780  | nan | nan |
| sudden | driverlog |open loop          | p01  | 0.973  | 0.837  | nan | nan |
| sudden | driverlog |closed loop ave    | p01  | 0.824  | 0.802  | nan | nan |
| sudden | driverlog |closed loop trend  | p01  | 0.716  | 0.803  | nan | nan |
| sudden | easy-ipc-grid |no relearn         | p5-5-5  | 0.803  | 0.648  | nan | nan |
| sudden | easy-ipc-grid |open loop          | p5-5-5  | 0.929  | 0.867  | nan | nan |
| sudden | easy-ipc-grid |closed loop ave    | p5-5-5  | 0.943  | 0.927  | nan | nan |
| sudden | easy-ipc-grid |closed loop trend  | p5-5-5  | 0.744  | 0.648  | nan | nan |
| sudden | blocks-world |no relearn         | p01  | 0.654  | 0.494  | nan | nan |
| sudden | blocks-world |open loop          | p01  | 0.557  | 0.508  | nan | nan |
| sudden | blocks-world |closed loop ave    | p01  | 0.949  | 0.815  | nan | nan |
| sudden | blocks-world |closed loop trend  | p01  | 0.923  | 0.773  | nan | nan |
| sudden | zeno-travel |no relearn         | p06  | 0.927  | 0.536  | nan | nan |
| sudden | zeno-travel |open loop          | p06  | 0.705  | 0.670  | nan | nan |
| sudden | zeno-travel |closed loop ave    | p06  | 0.753  | 0.760  | nan | nan |
| sudden | zeno-travel |closed loop trend  | p06  | 0.795  | 0.701  | nan | nan |
| sudden | satellite |no relearn         | p06  | 0.915  | 0.500  | nan | nan |
| sudden | satellite |open loop          | p06  | 0.929  | 0.834  | nan | nan |
| sudden | satellite |closed loop ave    | p06  | 0.862  | 0.687  | nan | nan |
| sudden | satellite |closed loop trend  | p06  | 0.736  | 0.696  | nan | nan |
| sudden | logistics |no relearn         | p07  | 0.950  | 0.787  | nan | nan |
| sudden | logistics |open loop          | p07  | 0.871  | 0.713  | nan | nan |
| sudden | logistics |closed loop ave    | p07  | 0.783  | 0.669  | nan | nan |
| sudden | logistics |closed loop trend  | p07  | 0.841  | 0.790  | nan | nan |
| sudden | satellite |no relearn         | p04  | 0.951  | 0.497  | nan | nan |
| sudden | satellite |open loop          | p04  | 0.833  | 0.690  | nan | nan |
| sudden | satellite |closed loop ave    | p04  | 0.995  | 0.778  | nan | nan |
| sudden | satellite |closed loop trend  | p04  | 0.874  | 0.547  | nan | nan |
| sudden | zeno-travel |no relearn         | p03  | 0.767  | 0.664  | nan | nan |
| sudden | zeno-travel |open loop          | p03  | 1.000  | 0.500  | nan | nan |
| sudden | zeno-travel |closed loop ave    | p03  | 0.772  | 0.400  | nan | nan |
| sudden | zeno-travel |closed loop trend  | p03  | 0.641  | 0.501  | nan | nan |
| sudden | logistics |no relearn         | p01  | 0.929  | 0.822  | nan | nan |
| sudden | logistics |open loop          | p01  | 0.620  | 0.507  | nan | nan |
| sudden | logistics |closed loop ave    | p01  | 0.711  | 0.865  | nan | nan |
| sudden | logistics |closed loop trend  | p01  | 0.891  | 0.535  | nan | nan |
| sudden | rovers |no relearn         | p03  | 0.915  | 0.781  | nan | nan |
| sudden | rovers |open loop          | p03  | 0.992  | 0.683  | nan | nan |
| sudden | rovers |closed loop ave    | p03  | 0.990  | 0.633  | nan | nan |
| sudden | rovers |closed loop trend  | p03  | 0.736  | 0.483  | nan | nan |
| sudden | driverlog |no relearn         | p02  | 0.779  | 0.554  | nan | nan |
| sudden | driverlog |open loop          | p02  | 1.000  | 0.889  | nan | nan |
| sudden | driverlog |closed loop ave    | p02  | 0.784  | 0.691  | nan | nan |
| sudden | driverlog |closed loop trend  | p02  | 0.530  | 0.499  | nan | nan |
| sudden | easy-ipc-grid |no relearn         | p5-10-10  | 0.758  | 0.570  | nan | nan |
| sudden | easy-ipc-grid |open loop          | p5-10-10  | 0.717  | 0.686  | nan | nan |
| sudden | easy-ipc-grid |closed loop ave    | p5-10-10  | 0.677  | 0.601  | nan | nan |
| sudden | easy-ipc-grid |closed loop trend  | p5-10-10  | 0.714  | 0.623  | nan | nan |
| sudden | logistics |no relearn         | p06  | 0.965  | 0.863  | nan | nan |
| sudden | logistics |open loop          | p06  | 0.613  | 0.500  | nan | nan |
| sudden | logistics |closed loop ave    | p06  | 0.757  | 0.690  | nan | nan |
| sudden | logistics |closed loop trend  | p06  | 0.814  | 0.706  | nan | nan |
| sudden | rovers |no relearn         | p07  | 1.000  | 0.767  | nan | nan |
| sudden | rovers |open loop          | p07  | 0.586  | 0.837  | nan | nan |
| sudden | rovers |closed loop ave    | p07  | 0.994  | 0.715  | nan | nan |
| sudden | rovers |closed loop trend  | p07  | 0.900  | 0.633  | nan | nan |
| sudden | logistics |no relearn         | p03  | 0.904  | 0.618  | nan | nan |
| sudden | logistics |open loop          | p03  | 1.000  | 0.790  | nan | nan |
| sudden | logistics |closed loop ave    | p03  | 0.736  | 0.813  | nan | nan |
| sudden | logistics |closed loop trend  | p03  | 0.578  | 0.595  | nan | nan |
| sudden | satellite |no relearn         | p07  | 0.907  | 0.500  | nan | nan |
| sudden | satellite |open loop          | p07  | 0.842  | 0.569  | nan | nan |
| sudden | satellite |closed loop ave    | p07  | 0.726  | 0.650  | nan | nan |
| sudden | satellite |closed loop trend  | p07  | 0.703  | 0.596  | nan | nan |
| sudden | miconic |no relearn         | p07  | 1.000  | 0.767  | nan | nan |
| sudden | miconic |open loop          | p07  | 0.816  | 0.746  | nan | nan |
| sudden | miconic |closed loop ave    | p07  | 0.955  | 0.811  | nan | nan |
| sudden | miconic |closed loop trend  | p07  | 0.753  | 0.682  | nan | nan |
| sudden | rovers |no relearn         | p07  | 1.000  | 0.876  | nan | nan |
| sudden | rovers |open loop          | p07  | 0.586  | 0.837  | nan | nan |
| sudden | rovers |closed loop ave    | p07  | 0.915  | 0.500  | nan | nan |
| sudden | rovers |closed loop trend  | p07  | 0.891  | 0.811  | nan | nan |
| sudden | satellite |no relearn         | p02  | 0.736  | 0.488  | nan | nan |
| sudden | satellite |open loop          | p02  | 0.772  | 0.890  | nan | nan |
| sudden | satellite |closed loop ave    | p02  | 1.000  | 0.962  | nan | nan |
| sudden | satellite |closed loop trend  | p02  | 0.950  | 0.787  | nan | nan |
| sudden | blocks-world |no relearn         | p01  | 0.654  | 0.500  | nan | nan |
| sudden | blocks-world |open loop          | p01  | 0.703  | 0.620  | nan | nan |
| sudden | blocks-world |closed loop ave    | p01  | 0.849  | 0.768  | nan | nan |
| sudden | blocks-world |closed loop trend  | p01  | 0.994  | 0.844  | nan | nan |
| sudden | logistics |no relearn         | p02  | 0.898  | 0.792  | nan | nan |
| sudden | logistics |open loop          | p02  | 0.726  | 0.702  | nan | nan |
| sudden | logistics |closed loop ave    | p02  | 0.717  | 0.686  | nan | nan |
| sudden | logistics |closed loop trend  | p02  | 0.995  | 0.850  | nan | nan |
| sudden | dwr |no relearn         | p01  | 0.874  | 0.736  | nan | nan |
| sudden | dwr |open loop          | p01  | 0.915  | 0.841  | nan | nan |
| sudden | dwr |closed loop ave    | p01  | 0.736  | 0.696  | nan | nan |
| sudden | dwr |closed loop trend  | p01  | 0.557  | 0.505  | nan | nan |
| sudden | dwr |no relearn         | p03  | 0.833  | 0.690  | nan | nan |
| sudden | dwr |open loop          | p03  | 0.842  | 0.864  | nan | nan |
| sudden | dwr |closed loop ave    | p03  | 0.598  | 0.496  | nan | nan |
| sudden | dwr |closed loop trend  | p03  | 0.613  | 0.488  | nan | nan |
| sudden | logistics |no relearn         | p03  | 0.955  | 0.811  | nan | nan |
| sudden | logistics |open loop          | p03  | 1.000  | 0.957  | nan | nan |
| sudden | logistics |closed loop ave    | p03  | 0.990  | 0.933  | nan | nan |
| sudden | logistics |closed loop trend  | p03  | 0.929  | 0.822  | nan | nan |
| sudden | satellite |no relearn         | p04  | 0.951  | 0.501  | nan | nan |
| sudden | satellite |open loop          | p04  | 0.620  | 0.504  | nan | nan |
| sudden | satellite |closed loop ave    | p04  | 0.530  | 0.499  | nan | nan |
| sudden | satellite |closed loop trend  | p04  | 0.884  | 0.835  | nan | nan |
| sudden | blocks-world |no relearn         | p02  | 0.621  | 0.508  | nan | nan |
| sudden | blocks-world |open loop          | p02  | 0.655  | 0.714  | nan | nan |
| sudden | blocks-world |closed loop ave    | p02  | 0.614  | 0.808  | nan | nan |
| sudden | blocks-world |closed loop trend  | p02  | 1.000  | 0.493  | nan | nan |
| sudden | logistics |no relearn         | p03  | 0.955  | 0.834  | nan | nan |
| sudden | logistics |open loop          | p03  | 1.000  | 0.876  | nan | nan |
| sudden | logistics |closed loop ave    | p03  | 0.671  | 0.622  | nan | nan |
| sudden | logistics |closed loop trend  | p03  | 0.893  | 0.796  | nan | nan |
| sudden | easy-ipc-grid |no relearn         | p5-5-5  | 0.784  | 0.661  | nan | nan |
| sudden | easy-ipc-grid |open loop          | p5-5-5  | 0.639  | 0.791  | nan | nan |
| sudden | easy-ipc-grid |closed loop ave    | p5-5-5  | 0.779  | 0.899  | nan | nan |
| sudden | easy-ipc-grid |closed loop trend  | p5-5-5  | 0.900  | 0.837  | nan | nan |
| sudden | intrusion-detection |no relearn         | p20  | 0.991  | 0.877  | nan | nan |
| sudden | intrusion-detection |open loop          | p20  | 0.915  | 0.828  | nan | nan |
| sudden | intrusion-detection |closed loop ave    | p20  | 0.530  | 0.499  | nan | nan |
| sudden | intrusion-detection |closed loop trend  | p20  | 0.836  | 0.855  | nan | nan |
| sudden | dwr |no relearn         | p01  | 0.874  | 0.745  | nan | nan |
| sudden | dwr |open loop          | p01  | 0.779  | 0.703  | nan | nan |
| sudden | dwr |closed loop ave    | p01  | 0.816  | 0.746  | nan | nan |
| sudden | dwr |closed loop trend  | p01  | 0.795  | 0.849  | nan | nan |
| sudden | easy-ipc-grid |no relearn         | p5-10-10  | 0.758  | 0.631  | nan | nan |
| sudden | easy-ipc-grid |open loop          | p5-10-10  | 0.703  | 0.600  | nan | nan |
| sudden | easy-ipc-grid |closed loop ave    | p5-10-10  | 0.898  | 0.808  | nan | nan |
| sudden | easy-ipc-grid |closed loop trend  | p5-10-10  | 0.736  | 0.488  | nan | nan |
| sudden | satellite |no relearn         | p03  | 0.606  | 0.496  | nan | nan |
| sudden | satellite |open loop          | p03  | 0.921  | 0.875  | nan | nan |
| sudden | satellite |closed loop ave    | p03  | 0.757  | 0.719  | nan | nan |
| sudden | satellite |closed loop trend  | p03  | 0.654  | 0.495  | nan | nan |
| sudden | logistics |no relearn         | p06  | 0.965  | 0.863  | nan | nan |
| sudden | logistics |open loop          | p06  | 1.000  | 0.957  | nan | nan |
| sudden | logistics |closed loop ave    | p06  | 0.726  | 0.696  | nan | nan |
| sudden | logistics |closed loop trend  | p06  | 1.000  | 0.889  | nan | nan |
| sudden | satellite |no relearn         | p06  | 0.915  | 0.500  | nan | nan |
| sudden | satellite |open loop          | p06  | 0.655  | 0.500  | nan | nan |
| sudden | satellite |closed loop ave    | p06  | 0.833  | 0.812  | nan | nan |
| sudden | satellite |closed loop trend  | p06  | 0.641  | 0.497  | nan | nan |

<br />

<br />


### Aggregated Statistics: percentage of improvement after environment changes

|                |  Open Loop  | Closed Loop Ave | Closed Loop Trend | BACC Drops |
| :------------: | :---------: | :-------------: | :---------------: | :--------: |
|   **Sudden**   | 62.0% / 10  |   33.5% / 1.4   |    51.6% / 2.3    |   0.170    |
|  **Gradual**   | 106.2% / 15 |   43.6% / 1.7   |    87.6% / 3.2    |   0.170    |
| **Reoccuring** | 62.3% / 20  |   36.1% / 3.4   |    51.5% / 5.4    |   0.167    |

