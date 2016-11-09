import java.io.*;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.TreeSet;


// FIXME Desempates por cartas mais altas
public class p054 {

  public class Carta implements Comparable<Carta>{
    private int valor;
    private char naipe;

    public Carta(int valor, char naipe){
      this.valor = valor;
      this.naipe = naipe;
    }
    public Carta(String valor, String naipe){
      switch (valor){
        case "J":
          this.valor = 11;
          break;
        case "Q":
          this.valor = 12;
          break;
        case "K":
          this.valor = 13;
          break;
        case "A":
          this.valor = 14;
          break;
        default:
          try{
            this.valor = Integer.parseInt(valor);
          }
          catch (Exception e){
            e.printStackTrace();
            this.valor = -1;
          }
      }
      this.naipe = naipe.charAt(0);
    }

    // s = "8C", "AD", etc..
    public Carta(String s){
      this.naipe = s.charAt(s.length()-1);
      String valor = s.substring(0,s.length()-1);
      switch (valor){
        case "T":
          this.valor = 10;
          break;
        case "J":
          this.valor = 11;
          break;
        case "Q":
          this.valor = 12;
          break;
        case "K":
          this.valor = 13;
          break;
        case "A":
          this.valor = 14;
          break;
        default:
          try{
            this.valor = Integer.parseInt(valor);
          }
          catch (Exception e){
            e.printStackTrace();
            this.valor = -1;
          }
      }
    }

    public boolean isRoyal(){
      return this.valor >= 10;
    }

    public int getValor(){
      return this.valor;
    }

    public float getValorNorm(){ return (this.valor-1)/14.0f;}

    public char getNaipe() {
      return naipe;
    }

    @Override
    public int compareTo(Carta carta) {
      if(this.getValor() >= carta.getValor())
          return 1;
      else return -1;
    }
  }

  public class Mao {
    private TreeSet<Carta> cartas;
    private ArrayList<Carta> altas;

    public TreeSet<Carta> getCartas(){
      return this.cartas;
    }

    public Mao(){
      this.cartas = new TreeSet<>();
    }

    public Mao(TreeSet<Carta> cartas) {
      this.cartas = cartas;
    }

    public void add(Carta c){
      this.cartas.add(c);
    }

    public float getPontos(){
      float pontos;
      if( (pontos = royalFlush()) > 0)
        return 10+pontos;
      else if( (pontos = straigthFlush()) > 0)
        return 9+pontos;
      else if( (pontos = fourOfAKind()) > 0)
        return 8+pontos;
      else if( (pontos = fullHouse()) > 0)
        return 7+pontos;
      else if( (pontos = flush()) > 0)
        return 6+pontos;
      else if( (pontos = straigth()) > 0)
        return 5+pontos;
      else if( (pontos = threeOfAKind()) > 0)
        return 4+pontos;
      else if( (pontos = twoPairs()) > 0)
        return 3+pontos;
      else if( (pontos = onePair()) > 0)
        return 2+pontos;
      else
        pontos = this.cartas.last().getValorNorm();
        return pontos;
    }

    private float royalFlush() {
      char naipe = cartas.first().getNaipe();
      for(Carta carta: this.cartas){
        if(carta.getNaipe() != naipe || !carta.isRoyal())
          return 0;
      }
      return cartas.last().getValorNorm();
    }

    private float straigthFlush() {
      Iterator<Carta> it = this.cartas.iterator();
      Carta carta = it.next();
      char naipe = carta.getNaipe();
      int valor = carta.getValor();
      while(it.hasNext()){
        carta = it.next();
        if(carta.getNaipe() != naipe || carta.getValor() != ++valor)
          return 0;
      }
      return cartas.last().getValorNorm();
    }

    private int countOfAKind(int valor){
      int count = 0;
      for(Carta carta: this.cartas){
        if(carta.getValor() == valor)
          count++;
      }
      return count;
    }

    private float fourOfAKind() {
      Iterator<Carta> it = this.cartas.iterator();
      int i = 0;
      while(it.hasNext() && i<2){
        Carta carta = it.next();
        if(this.countOfAKind(carta.getValor()) == 4)
          return carta.getValorNorm();
        i++;
      }
      return 0;
    }

    private float fullHouse() {
      float pontos = 0;
      if( (pontos = this.threeOfAKind()) > 0
          && this.onePair() > 0)
        return pontos;
      else return 0;
    }
    
    private float flush(){
      Iterator<Carta> it = this.cartas.iterator();
      char naipe = it.next().getNaipe();
      while(it.hasNext()){
        Carta carta = it.next();
        if(carta.getNaipe() != naipe)
          return 0;
      }
      return cartas.last().getValorNorm();
    }

    private float straigth() {
      Iterator<Carta> it = this.cartas.iterator();
      int valor = it.next().getValor();
      while(it.hasNext()){
        Carta carta = it.next();
        if(carta.getValor() != ++valor)
          return 0;
      }
      return cartas.last().getValorNorm();
    }

    private float threeOfAKind() {
      Iterator<Carta> it = this.cartas.iterator();

      int i = 0;
      while(it.hasNext() && i<3){
        Carta carta = it.next();
        if(this.countOfAKind(carta.getValor()) == 3)
          return carta.getValorNorm();
        i++;
      }
      return 0;
    }

    private float twoPairs() {
      boolean umPar = false;
      Carta par1 = null;
      float r1,r2;
      Iterator<Carta> it = this.cartas.iterator();
      while(it.hasNext()){
        Carta carta = it.next();
        if(this.countOfAKind(carta.getValor()) == 2){
          if(!umPar){
            umPar = true;
            par1 = carta;
          }
          else if(carta.getValor() != par1.getValor())
            if( (r1=carta.getValorNorm()) > (r2=par1.getValorNorm()))
              return r1+0.0001f*r2;
          else
            return r2+0.0001f*r1;
        }
      }
      return 0;
    }

    private float onePair() {
      Iterator<Carta> it = this.cartas.iterator();
      int i = 0;
      while(it.hasNext() && i<4){
        Carta carta = it.next();
        if(this.countOfAKind(carta.getValor()) == 2)
          return carta.getValorNorm();
        i++;
      }
      return 0;
    }

    public boolean wins(Mao other){
      return this.getPontos() > other.getPontos();
    }
  }

  public void start(BufferedReader reader) throws IOException {
    String line = null;
    int vitorias = 0;
    while( (line = reader.readLine()) != null ){
      Mao m1 = new Mao();
      Mao m2 = new Mao();
      String[] split = line.split(" ");
      for(int i = 0; i<5; i++){
        m1.add(new Carta(split[i]));
      }
      for(int i = 5; i<10; i++){
        m2.add(new Carta(split[i]));
      }
      if(m1.wins(m2))
        vitorias++;
    }
    System.out.println("Vitorias do jogador 1 >> " + vitorias);
  }

  public static void main(String[] args) throws IOException {
    if(args.length != 1){
      System.out.println("Erro: Ficheiro deve ser passado como argumento");
      return;
    }

    BufferedReader reader = new BufferedReader(new FileReader(args[0]));
    new p054().start(reader);
  }
}