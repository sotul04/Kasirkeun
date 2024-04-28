/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package entity;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/**
 *
 * @author Suthasoma
 */
public class Transaction {
    
    private int idTransaction;
    private int couponFree;
    private int couponDiscount;
    private List<Pair<Integer, Integer>> items = new ArrayList<>();
    private double totalPrice;
    private String datetime;
    private double discount;

    /**
     * @return the idTransaction
     */
    public int getIdTransaction() {
        return idTransaction;
    }

    /**
     * @param idTransaction the idTransaction to set
     */
    public void setIdTransaction(int idTransaction) {
        this.idTransaction = idTransaction;
    }

    /**
     * @return the couponFree
     */
    public int getCouponFree() {
        return couponFree;
    }

    /**
     * @param couponFree the couponFree to set
     */
    public void setCouponFree(int couponFree) {
        this.couponFree = couponFree;
    }

    /**
     * @return the couponDiscount
     */
    public int getCouponDiscount() {
        return couponDiscount;
    }

    /**
     * @param couponDiscount the couponDiscount to set
     */
    public void setCouponDiscount(int couponDiscount) {
        this.couponDiscount = couponDiscount;
    }

    /**
     * @return the items
     */
    public List<Pair<Integer, Integer>> getItems() {
        return items;
    }

    /**
     * @param items the items to set
     */
    public void setItems(ArrayList<Pair<Integer, Integer>> items) {
        this.items = items;
    }

    /**
     * @return the totalPrice
     */
    public double getTotalPrice() {
        return totalPrice;
    }

    /**
     * @param totalPrice the totalPrice to set
     */
    public void setTotalPrice(double totalPrice) {
        this.totalPrice = totalPrice;
    }

    /**
     * @return the date time
     */
    public String getDatetime() {
        return datetime;
    }

    /**
     * @param datetime the date time to set
     */
    public void setDatetime(String datetime) {
        this.datetime = datetime;
    }

    /**
     * @return the discount
     */
    public double getDiscount() {
        return discount;
    }

    /**
     * @param discount the discount to set
     */
    public void setDiscount(double discount) {
        this.discount = discount;
    }
    
    /**
     addition
     */
    public Pair<Integer, Integer> getItem(int index) {
        return items.get(index);
    }
    
    public void setItem(int index, Pair<Integer, Integer> item) {
        items.set(index, item);
    }
    
    public int getItemPosition(Pair<Integer, Integer> item) {
        for (int i = 0; i < items.size(); i++) {
            if (Objects.equals(items.get(i).getFirst(), item.getFirst())) {
                return i;
            }
        }
        return -1;
    }
    
    public void add(Pair<Integer, Integer> item) {
        int pos = getItemPosition(item);
        if (pos < 0) {
            items.add(item);
        } else {
            item.setSecond(item.getSecond() + items.get(pos).getSecond());
            items.set(pos, item);
        }   
    }
}
