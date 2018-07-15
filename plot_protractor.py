import numpy as np
import matplotlib.pyplot as plt
def plot_protractor():    
    # ====================================== draw a protractor ======================================
    radius = 1.8; npoints = 30;
    angle = 0.0*np.pi/180.0;
    x_df = np.cos(angle)*radius; 
    x_dummy = np.linspace(0.0, x_df, npoints);
    y_dummy = np.zeros((x_dummy.shape[0]));
    plt.plot(x_dummy, np.tan(angle, out = y_dummy)*x_dummy, '.k', markevery=4, alpha=0.1);
    angle = 15.0*np.pi/180.0;
    x_df = np.cos(angle)*radius;
    x_dummy = np.linspace(0.0, x_df, npoints);
    plt.plot(x_dummy, np.tan(angle, out = y_dummy)*x_dummy, '.k', markevery=4, alpha=0.1);
    angle = 30.0*np.pi/180.0;
    x_df = np.cos(angle)*radius; 
    x_dummy = np.linspace(0.0, x_df, npoints);
    plt.plot(x_dummy, np.tan(angle, out = y_dummy)*x_dummy, '.k', markevery=4, alpha=0.1);
    angle = 45.0*np.pi/180.0;
    x_df = np.cos(angle)*radius; 
    x_dummy = np.linspace(0.0, x_df, npoints);
    plt.plot(x_dummy, np.tan(angle, out = y_dummy)*x_dummy, '.k', markevery=4, alpha=0.1);
    angle = 60.0*np.pi/180.0;
    x_df = np.cos(angle)*radius; 
    x_dummy = np.linspace(0.0, x_df, npoints);
    plt.plot(x_dummy, np.tan(angle, out = y_dummy)*x_dummy, '.k', markevery=4, alpha=0.1);
    angle = 75.0*np.pi/180.0;
    x_df = np.cos(angle)*radius;
    x_dummy = np.linspace(0.0, x_df, npoints);
    plt.plot(x_dummy, np.tan(angle, out = y_dummy)*x_dummy, '.k', markevery=4, alpha=0.1);
    angle = 90.0*np.pi/180.0;
    x_df = np.cos(angle)*radius; 
    x_dummy = np.linspace(0.0, x_df, npoints);
    plt.plot(x_dummy, np.tan(angle, out = y_dummy)*x_dummy, '.k', markevery=4, alpha=0.1);

    x_dummy = np.linspace(0.0, 1.8, npoints);
    plt.plot(x_dummy, np.sqrt(1.8**2 - x_dummy**2), '-k', markevery = 1, alpha=0.1);
    # =============================================================================================
    return 0;
