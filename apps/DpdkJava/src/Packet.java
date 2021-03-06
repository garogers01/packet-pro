/*
 * Generic packet class to store native pointers to the data
 */

public abstract class Packet {
	
	protected long mbuf_pointer;
	protected long packet_pointer;
	
	protected UnsafeAccess ua;
	
	public static final int IPV4 = 4;
	public static final int IPV6 = 6;
	
	public Packet(long mbuf, long packet, UnsafeAccess unsafe) {
		mbuf_pointer = mbuf;
		packet_pointer = packet;
		ua = unsafe;
		ua.setCurrentPointer(packet_pointer);
	}

	public long getMbuf_pointer() {
		return mbuf_pointer;
	}

	public void setMbuf_pointer(long mbuf_pointer) {
		this.mbuf_pointer = mbuf_pointer;
	}

	public long getPacket_pointer() {
		return packet_pointer;
	}

	public void setPacket_pointer(long packet_pointer) {
		this.packet_pointer = packet_pointer;
	}

	public int whichIP() {
		ua.setCurrentPointer(packet_pointer);
		int version = ua.getByte() >> 4;
		if (version == IPV4 || version == IPV6) {
			return version;
		} else {
			return 0;
		}
	}
	
	public abstract String toString();
	public abstract int getLength();
	public abstract int getVersion();
	
}