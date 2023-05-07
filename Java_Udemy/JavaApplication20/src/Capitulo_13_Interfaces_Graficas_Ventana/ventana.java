package Capitulo_13_Interfaces_Graficas_Ventana;

import java.awt.Color;
import java.awt.Dimension;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class ventana extends JFrame {

    public ventana() {
        this.setSize(500, 500); //Establecemos el tamaño de la ventana
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);//Cierra la ventana
        this.setTitle("El mejor titulo");//Establecemos el titulo de la ventana       
        //this.setLocation(100, 200); //Establecemos la posicion inicial
        //this.setBounds(100, 200, 500, 500);//Engloba tanto el setSize como el setLocation
        //Por orden (x,y(de posicion) ancho y largo(tamaño de la ventana))
        this.setLocationRelativeTo(null); //Tu ventana aparece en el centro de la pantalla

        //this.setResizable(false);//Establecemos si la ventana puede cambiar de tamaño
        this.setMinimumSize(new Dimension(300,300));//Establecemos el tamaño minimo
        
        //this.getContentPane().setBackground(Color.BLACK); //Cambia el fondo de la ventana
        
        iniciarComponentes();
        
        
    }
    
    private void iniciarComponentes(){
        JPanel panel = new JPanel(); //Creacion de un panel
        this.getContentPane().add(panel); //Agregamos el panel a la ventana
        //panel.setBackground(Color.GREEN); //Establecemos color al panel
        
    }

}
